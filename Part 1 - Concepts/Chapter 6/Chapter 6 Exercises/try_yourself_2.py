# glossary = {
#     "interpreter": "Program that executes code line-by-line without compiling it into a separate executable.",
#     "if": "A conditional statement to make decision based on a condition.",
#     "for": "A loop that executes a specific number of times based on condition.",
#     "while": "A loop that executes as long as a condition remains true.",
#     "boolean expression": "An expression that returns either True or False.",
#     "python": "A high-level, interpreted, general-purpose programming language known for its readability and versatility.",
#     "set": "Unordered collection of unique, hashable elements.",
#     "list": "Ordered mutable collection that can hold elements of any data type.",
#     "dictionaries": "Unordered, mutable collection of key-value pairs.",
#     "variable": "Named storage location in a program that holds a value which can change during execution.",
# }


# i = 1
# for word in glossary:
#     print(f"{i} {word.title()} : {glossary[word]}")
#     i += 1

# rivers = {
#     "nile": "egypt",
#     "amazon": "brazil",
#     "yangtze": "china",
# }

# for river, country in rivers.items():
#     print(f"The {river.title()} runs through {country.title()}.")

# for river in rivers.keys():
#     print(river)

# for country in rivers.values():
#     print(country)

favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

poll_takers = ["john", "bob", "clarissa", "wanda", "biden"]

for poll_taker in poll_takers:
    if poll_taker in favourite_languages.keys():
        print(f"Thank you {poll_taker.title()} for taking part in the poll!")
    else:
        print(f"Please {poll_taker.title()}, take part in the poll!")
