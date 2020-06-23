


import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",
    fill_color=color_producer(el), fill=True,  color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


name=["Great Wall of china (Border of china)","Petra (Jordan)","Christ The Redeemer (Brazil)","Machu Picchu (peru)","Chichen Itza (Mexico)","Colosseum (Rome)","Taj Mahal (India)"]
lat1=["40.431908","30.329002"," -22.951871","-13.163068","20.6667","41.890251","27.173891"]
lon1=["116.570374","35.444665","-43.21118","-72.545128","-88.5667","12.492373","78.042068"]

fgw=folium.FeatureGroup(name="The Seven Wonders of The World")
for lt,ln,na in zip(lat1,lon1,name):
    fgw.add_child(folium.Marker(location=[lt,ln], popup=na,icon=folium.Icon(color='blue')))

map.add_child(fgw)
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
