def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']}, z miejscowości: {user['location']} opublikował {user['posts']} postów")


def add_user(users_data: list) -> None:
    new_name = input('podaj imię nowego uzytkownika: ')
    new_location = input('podaj lokalizację uzytkownika: ')
    new_posts = int(input('podaj liczbę postów nowego uzytkownika: '))
    users_data.append({"name": new_name, "location": new_location, "posts": new_posts}, )

def remove_user(users_data: list) -> None:
    uzytkownik_do_usunięcia = input('podaj uzytkownika do usuniecia: ')

    for user in users_data:
        if user['name'] == uzytkownik_do_usunięcia:
            users_data.remove(user)

def update_user(users_data: list) -> None:

    uzytkownik_do_edycji = input('podaj uzytkownik do edycja: ')
    for user in users_data:
        if user['name'] == uzytkownik_do_edycji:
            user['name'] = input('podaj nowe imie uzytkownika:')
            user['location'] = input('podaj nową lokalizację uzytkownik:')
            user['posts'] = int(input('podaj nowa liczbe postów:'))


def get_map(users_dat: list) -> None:
    import folium
    map = folium.Map(location=(52.23, 21.00), zoom_start=6)
    for user in users_data:
        cooridinates = get_coordinates(user["location"])

        folium.Marker(
            location=(coordinates[0], coordinates[1]),
            popup=f"<img src={user['image']} <br/> miejscowość: {user['location']} opublikował {user['posts']} postów").add_to(
            map)
    map.save('mapa.html')
