users = [
    {"name": "Damian", "location": "Kraków", "posts": 555},
]


def remove_user(users_data: list) -> None:
    uzytkownik_do_usunięcia = input('podaj uzytkownika do usuniecia: ')

    for user in users_data:

        if user['name'] == uzytkownik_do_usunięcia:
            users_data.remove(user)


print(users)
