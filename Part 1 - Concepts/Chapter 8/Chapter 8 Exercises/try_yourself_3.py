# def city_country(city, country):
#     return f"{city} {country}".title()


# c1 = city_country("Islamabad", "Pakistan")
# c2 = city_country("Santiago", "Chile")
# c3 = city_country("Beijing", "China")

# print(c1)
# print(c2)
# print(c3)


def make_album(artist_name, album_title, num_songs=None):
    album = {"artist": artist_name, "title": album_title}

    if num_songs:
        album["Number of songs"] = num_songs
    return album


# album1 = make_album("Arijit Singh", "Aashiqui 2")
# album2 = make_album("Arijit Singh", "Bekhayali")
# album3 = make_album("Atif Aslam", "Meri Kahani")
# album4 = make_album("Arijit Singh", "Ae Dil Hai Mushkil", "11")

# print(album1)
# print(album2)
# print(album3)
# print(album4)

while True:
    print("Press 'q' any time to quit!")
    artist = input("\nEnter your favourite artist's name: ")
    if artist == "q":
        break

    title = input("Enter their favourite album: ")
    if title == "q":
        break

    album = make_album(artist, title)
    print(album)
