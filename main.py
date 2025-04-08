user = [
    {"name": "Damian", "location": "Kraków", "posts": 555},
    {"name": "Mikołaj", "location": "Przasnysz", "posts": 200},
    {"name": "Krzysztof", "location": "Poznań", "posts": 100},
    {"name": "Bartosz", "location": "Ostrołęka", "posts": 300},

]

for user in users:
    print(f"Twój znajomy {user['name']}, z {user['location']} opublikował {user['posts']} postów")
