import folium
import pandas

volc_data = pandas.read_csv("Volcanoes.txt")
lon =  list(volc_data["LON"])
lat =  list(volc_data["LAT"])
elev = list(volc_data["ELEV"])

def conditional_el(el_var):
    if el_var > 0 and el_var < 1000:
        return 'green'
    elif el_var < 3000 and el_var > 1000:
        return 'orange'
    elif el_var > 3000:
        return 'red'
    else:
        return 'black'

map = folium.Map(location=[35.58, -99.09], zoom_start=5, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt,ln], popup="Elevation: " + str(int(el)), radius=10, fill_color=conditional_el(el),color='white', fill_opacity=0.9))

fgp = folium.FeatureGroup(name='population')

fgp.add_child(folium.GeoJson(data = open('world.json','r',encoding = 'utf-8-sig').read(), 
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("First_Map.html") 
