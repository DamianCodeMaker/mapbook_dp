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
        if user['name'] == uzytkownik_do_usuniecia:
            users_data.remove(user)
