import folium
import webbrowser
import gpxpy
import os

def overlayGPX(gpxData, map, status):
    gpx_file = open(gpxData, 'r')
    gpx = gpxpy.parse(gpx_file)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:        
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))

    if status == 1: folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(map)
    elif status == 2: folium.PolyLine(points, color="purple", weight=2.5, opacity=1).add_to(map)
    elif status == 3: folium.PolyLine(points, color="green", weight=2.5, opacity=1).add_to(map)

myMap = folium.Map(location=[10,10],zoom_start=3)

for file in os.listdir("routes"):
    if file.endswith(".gpx"):
        path = os.path.join("routes", file)
        overlayGPX(path, myMap, 2)

myMap.save('index.html')
webbrowser.open('index.html')