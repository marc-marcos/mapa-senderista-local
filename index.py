import folium
import webbrowser
import gpxpy
import sqlite3

BASE_PATH = 'routes/'

def overlayGPX(gpxData, map, status):
    gpx_file = open(gpxData, 'r')
    gpx = gpxpy.parse(gpx_file)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:        
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))

    if status == 0: folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(map)
    elif status == 1: folium.PolyLine(points, color="purple", weight=2.5, opacity=1).add_to(map)
    elif status == 2: folium.PolyLine(points, color="green", weight=2.5, opacity=1).add_to(map)

myMap = folium.Map(location=[10,10],zoom_start=3)

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('SELECT * FROM routes')
rows = c.fetchall()

for row in rows:
    overlayGPX(BASE_PATH + row[0], myMap, row[2])

myMap.save('index.html')
webbrowser.open('index.html')