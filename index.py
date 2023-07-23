import folium
import webbrowser
import gpxpy
import sqlite3

BASE_PATH = 'routes/'

def overlayGPX(gpxData, map, status, customText = None, customShortText = None):
    gpx_file = open(gpxData, 'r')
    gpx = gpxpy.parse(gpx_file)
    points = []

    customShortText = gpx.tracks[0].name
    distance = gpx.length_3d()
    totalElevation = gpx.get_uphill_downhill()
    customText = "<b>Distance:</b> " + str(round(distance/1000, 2)) + " km" + "<br>" + "<b>Elevation:</b> " + str(round(totalElevation[0], 2)) + " m"



    for track in gpx.tracks:
        for segment in track.segments:        
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))

    if status == 0: 
        folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(map)
        statusColor = "red"
    elif status == 1: 
        folium.PolyLine(points, color="purple", weight=2.5, opacity=1).add_to(map)
        statusColor = "purple"
    elif status == 2: 
        folium.PolyLine(points, color="green", weight=2.5, opacity=1).add_to(map)
        statusColor = "green"
    else: 
        folium.PolyLine(points, color="blue", weight=2.5, opacity=1).add_to(map)
        statusColor = "blue"

    folium.Marker(
        [gpx.tracks[0].segments[0].points[0].latitude, 
        gpx.tracks[0].segments[0].points[0].longitude], 
        popup=customText,
        icon=folium.Icon(color=statusColor),
        tooltip=customShortText).add_to(map)

myMap = folium.Map(location=[10,10],zoom_start=3)

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('SELECT * FROM routes')
rows = c.fetchall()

for row in rows:
    overlayGPX(BASE_PATH + row[0], myMap, row[2], row[1])

myMap.save('index.html')
webbrowser.open('index.html')