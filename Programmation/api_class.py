import folium
import requests
import time


"""nb_positions = 10
nb_secondes = 2

donnees_ISS=requests.get('http://api.open-notify.org/iss-now.json').json()
coords = (float(donnees_ISS["iss_position"]["longitude"]), float(donnees_ISS["iss_position"]["latitude"]))
fmap = folium.Map(location=coords, tiles="OpenStreetMap", zoom_start=6)

positions = []

for i in range(nb_positions):
    print(i)
    donnees_ISS=requests.get('http://api.open-notify.org/iss-now.json').json()
    coords = (float(donnees_ISS["iss_position"]["longitude"]), float(donnees_ISS["iss_position"]["latitude"]))
    positions.append(coords)

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    folium.Marker(location=coords, popup=f"{current_time}").add_to(fmap)
    time.sleep(nb_secondes)

folium.PolyLine(positions, color="blue", weight=2.5, opacity=0.8).add_to(fmap)
fmap.save(outfile="test_mp.html")"""



url="https://opendata.lillemetropole.fr/explore/dataset/vlille-realtime/download/?format=json&timezone=Europe/Paris&lang=fr"

data = requests.get(url).json()

coords_list = []
locations = []
for local in data:
    name = local["fields"]["nom"]
    location = {"coords": local["fields"]["geo"], "name":name, "velo_dispo":local["fields"]["nbvelosdispo"], "place_dispo":local["fields"]["nbplacesdispo"]}
    locations.append(location)


coords = (data[0]["fields"]["geo"])
fmap = folium.Map(location=coords, tiles="OpenStreetMap", zoom_start=12)

for place in locations:
    coords = place["coords"]
    place_name = place["name"]
    n_velo_dispo = place["velo_dispo"]
    place_dispo = place["place_dispo"]
    if n_velo_dispo >= 12:
        folium.Marker(location=coords, popup=f"{place_name}, Nb.Velo : {n_velo_dispo} Nb.Place : {place_dispo}", icon=folium.Icon(color='green')).add_to(fmap)
    elif n_velo_dispo >= 1:
        folium.Marker(location=coords, popup=f"{place_name}, Nb.Velo : {n_velo_dispo} Nb.Place : {place_dispo}", icon=folium.Icon(color='orange')).add_to(fmap)
    elif n_velo_dispo == 0:
        folium.Marker(location=coords, popup=f"{place_name}, Nb.Velo : {n_velo_dispo} Nb.Place : {place_dispo}", icon=folium.Icon(color='red')).add_to(fmap)

fmap.save(outfile="test_mp.html")