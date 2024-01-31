import sqlite3
import folium
import webbrowser
import gpxpy


def startupMap():
    BASE_PATH = 'routes/'
    BASE_PATH_CACHE = 'caches/'

    myMap = folium.Map(location=[10, 10], zoom_start=3)

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('SELECT * FROM routes')
    rows = c.fetchall()

    for row in rows:
        overlayGPX(BASE_PATH + row[0], myMap, row[2], row[1])
    
    c.execute('SELECT * FROM caches')
    rows2 = c.fetchall()

    for row in rows2:
        overlayGPX_cache(BASE_PATH_CACHE + row[0], myMap, row[2], row[1])

    myMap.save('index.html')
    webbrowser.open('index.html')

def overlayGPX_cache(gpxData, map, status, customText=None):
    gpx_file = open(gpxData, 'r')
    gpx = gpxpy.parse(gpx_file)

    lon = gpx.waypoints[0].longitude
    lat = gpx.waypoints[0].latitude

    if status == 1:
        folium.Marker((lat, lon), tooltip=customText, color="red", icon=folium.Folium(color="red")).add_top(map)

    elif status == 2:
        folium.Marker((lat, lon), tooltip=customText, color="red", icon=folium.Icon(color="purple")).add_to(map)

    elif status == 3:
        folium.Marker((lat, lon), tooltip=customText, color="red", icon=folium.Icon(color="green")).add_to(map)

    else:
        folium.Marker((lat, lon), tooltip=customText, color="red", icon=folium.Icon(color="blue")).add_to(map)


def overlayGPX(gpxData, map, status, customText=None, customShortText=None):
    gpx_file = open(gpxData, 'r')
    gpx = gpxpy.parse(gpx_file)
    points = []

    customShortText = gpx.tracks[0].name
    distance = gpx.length_3d()
    totalElevation = gpx.get_uphill_downhill()

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))

    if status == 0:
        folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(map)
        statusColor = "red"
    elif status == 1:
        folium.PolyLine(points, color="purple",
                        weight=2.5, opacity=1).add_to(map)
        statusColor = "purple"
    elif status == 2:
        folium.PolyLine(points, color="green",
                        weight=2.5, opacity=1).add_to(map)
        statusColor = "green"
    else:
        folium.PolyLine(points, color="blue", weight=2.5,
                        opacity=1).add_to(map)
        statusColor = "blue"

    customText = f"<b>Distance:</b> {round(distance/1000, 2)} km\n<b>Elevation:</b> {round(totalElevation[0])} m"

    folium.Marker(
        [gpx.tracks[0].segments[0].points[0].latitude,
         gpx.tracks[0].segments[0].points[0].longitude],
        popup=customText,
        icon=folium.Icon(color=statusColor),
        tooltip=customShortText).add_to(map)
