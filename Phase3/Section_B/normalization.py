import json

games = [
    {
        "id": 101,
        "title": "Elden Ring",
        "developer": {
            "name": "FromSoftware",
            "country": "Japan",
            "website": "fromsoftware.jp"
        },
        "genres": [
            {"name": "RPG"},
            {"name": "Action"}
        ],
        "rating": {
            "score": 9.5,
            "votes": 5000
        }
    },
    {
        "id": 102,
        "title": "Cyberpunk 2077",
        "developer": {
            "name": "CD Projekt Red",
            "country": "Poland",
            "website": "cdprojektred.com"
        },
        "genres": [
            {"name": "RPG"},
            {"name": "Open World"}
        ],
        "rating": {
            "score": 8.8,
            "votes": 4200
        }
    },
    {
        "id": 103,
        "title": "Forza Horizon 5",
        "developer": {
            "name": "Playground Games",
            "country": "United Kingdom",
            "website": "playground-games.com"
        },
        "genres": [
            {"name": "Racing"},
            {"name": "Open World"}
        ],
        "rating": {
            "score": 9.0,
            "votes": 3800
        }
    },
    {
        "id": 104,
        "title": "God of War Ragnarök",
        "developer": {
            "name": "Santa Monica Studio",
            "country": "USA",
            "website": "sms.playstation.com"
        },
        "genres": [
            {"name": "Action"},
            {"name": "Adventure"}
        ],
        "rating": {
            "score": 9.3,
            "votes": 4600
        }
    }
]

# suppose lets assume we want id 102 details;
clean_game = []

for index in games:
    if index['id'] == 102 or index['id'] == 104:
        clean_game.append({
            'id':index['id'],
            'title':index['title'],
            'developer':index['developer']['name'],
            'developer country':index['developer']['country'],
            'developer website':index['developer']['website'],
            'genres':index['genres'],
            'rating':index['rating']['score'],
            'votes':index['rating']['votes']}
            )

print(json.dumps(clean_game,indent=4))