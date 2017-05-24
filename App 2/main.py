import folium
import pandas

def getColor(elev):
    if elev in range(0, 1000):
        return 'green'
    elif elev in range(1000, 3000):
        return 'orange'
    else:
        return 'red'

df = pandas.read_csv("Volcanoes-USA.txt")
map = folium.Map(location=[45.372, -121.697], zoom_start=12, tiles="Mapbox bright")
# map.simple_marker(location=[45.427334, -75.683593], marker_color="red", popup="Home")
# map.simple_marker(location=[45.399422, -75.735540], marker_color="blue", popup="Work")

fg=folium.FeatureGroup(name="volcano locations")

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    # map.simple_marker(location=[lat, lon], marker_color=getColor(elev), popup=name)
    fg.add_child(folium.Marker(location=[lat, lon], icon=folium.Icon(color=getColor(elev)), popup=name))

map.add_child(fg)

map.add_child(folium.GeoJson(data=open('World_population.json'),
name="World Population",
style_function=lambda x: {'fillcolor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(folium.LayerControl())

map.save(outfile="test.html")
