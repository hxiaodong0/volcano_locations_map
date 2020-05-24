import folium
import pandas

data = pandas.read_csv("/Users/xiaodonghuo/PycharmProjects/map_project/Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data["ELEV"])

# print(data)
# type(data)
# data["NAME"]
def color_producer(elevation):
    if elevation <1000:
        return "darkgreen"
    if 1000<elevation<1500:
        return 'green'
    if 1500<elevation<2000:
        return "orange"
    if 2000<elevation<2500:
        return 'red'
    else:
        return 'darkred'

def color_producer001(population):
    if population <1000000:
        return "darkgreen"
    if 1000000<population<10000000:
        return 'green'
    if 10000000<population<100000000:
        return "orange"
    if 100000000<population<250000000:
        return 'red'
    else:
        return 'black'

# lst = {'California Institute of Technology': [34.138221, -118.126218],'Stanford University':[37.427151, -122.170502],'Johns hopkins':[39.320845, -76.621218]}
# name = ['California Institute of Technology','Stanford University','Johns hopkins']

map1 = folium.Map(location=[40.031339, -98.998880],zoom_start=5)#tiles="Stamen Terrain"
fgV = folium.FeatureGroup(name = "Volcanoes")

for la,ln,el in zip(lat, lon , elev):
    fgV.add_child(folium.Marker( location=[la, ln], popup=str(el) + 'm', icon=folium.Icon(color=color_producer(el))))

fgP = folium.FeatureGroup(name = "Population ")


fgP.add_child(folium.GeoJson(data=open('/Users/xiaodonghuo/PycharmProjects/map_project/world.json','r', encoding= 'utf-8-sig').read(),
                            style_function= lambda x: {'fillColor': color_producer001(x['properties']['POP2005']) } ))

map1.add_child(fgV)
map1.add_child(fgP)
map1.add_child(folium.LayerControl())
map1.save("Map1.html")

# map1.add_child(folium.CircleMarker(radius = 5, location = [la,ln], popup= str(el) + 'm',  fill_color	= color_producer(el), color = '', fill_opacity=1 ))
