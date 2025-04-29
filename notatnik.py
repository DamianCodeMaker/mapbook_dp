users = [
    {"name": "Damian", "location": "Kraków", "posts": 555},
    {"name": "Mikołaj", "location": "Przasnysz", "posts": 200},
    {"name": "Krzysztof", "location": "Poznań", "posts": 100},
    {"name": "Bartosz", "location": "Ostrołęka", "posts": 300},
]


import folium
import requests
from bs4 import BeautifulSoup

#https://pl.wikipedia.org/wiki/Przybysławice_(województwo_lubelskie)

def get_cooridinates(city:str)->list:

    url=f'https://pl.wikipedia.org/wiki/{city}'
    response = requests.get(url).text
    response_html = BeautifulSoup(response, 'html.parser')
    longitude =float( response_html.select('.longitude')[0].text. replace(',', '.'))
    latitude =float( response_html.select('.latitude')[1].text.replace(',', '.'))
    return [longitude, latitude]


def get_map(users_dat:list)-> None:
    map = folium.Map(location=(52.23, 21.00), zoom_start=6)
    for user in users_data:
        import folium
        coordinates=get_coordinates(user["location"])

        folium.Marker(
            location=(coordinates[0], coordinates[1]),
            popup=f"<img src={user['image']} <br/> miejscowość: {user['location']} opublikował {user['posts']} postów").add_to(
            map)
    map.save('mapa.html')

get_map(users)