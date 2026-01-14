# people = [
#     {
#         "first_name": "abdul",
#         "last_name": "basit",
#         "age": 20,
#         "city": "sohawa",
#     },
#     {
#         "first_name": "ali",
#         "last_name": "faizan",
#         "age": 20,
#         "city": "rawalpindi",
#     },
#     {
#         "first_name": "muhammad",
#         "last_name": "zulqarnain",
#         "age": 20,
#         "city": "rawalpindi",
#     },
# ]
# for person in people:
#     full_name = f"{person['first_name'].title()} {person['last_name'].title()}"

#     print(
#         f"The person's full name is {full_name}. The person is {person['age']} years old, and lives in {person['city'].title()}."
#     )

# pets = [
#     {
#         "kind": "cat",
#         "owner_name": "imchael",
#     },
#     {
#         "kind": "dog",
#         "owner_name": "catherine",
#     },
#     {
#         "kind": "parrot",
#         "owner_name": "joseph",
#     },
# ]

# for pet in pets:
#     print(
#         f"The kind of pet is {pet['kind']} and its owner is {pet['owner_name'].title()}"
#     )

# favourite_places = {
#     "Sameer": [
#         "Eiffel Tower",
#     ],
#     "Bob": ["Taj Mahal", "Pyramids of Giza", "Colosseum"],
#     "Diana": ["Statue of Liberty", "Maldives"],
# }

# for name, favourite_place in favourite_places.items():
#     print(f"\n{name}'s favourite places are: ")
#     for fav_place in favourite_place:
#         print(f"\t{fav_place}")

# favourite_numbers = {
#     "alice": [4, 11],
#     "bob": [9, 71],
#     "clark": [21, 13],
#     "stephen": [37, 96],
#     "troy": [55, 48],
# }

# for name, favourite_number in favourite_numbers.items():
#     print(f"\n{name.title()}'s favourite numbers are:")
#     for fav_num in favourite_number:
#         print(f"\t{fav_num}")

cities = {
    "Paris": {
        "country": "France",
        "population": "about 2.1 million",
        "fact": "It is known as the City of Light.",
    },
    "Tokyo": {
        "country": "Japan",
        "population": "about 14 million",
        "fact": "It is the largest metropolitan area in the world.",
    },
    "New York": {
        "country": "United States",
        "population": "about 8.3 million",
        "fact": "It is home to Central Park.",
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city}")
    for key, info in city_info.items():
        print(f"\t{key.title()}: {info}")
