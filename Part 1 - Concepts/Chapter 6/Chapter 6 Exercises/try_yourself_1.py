# person = {
#     "first_name": "abdul",
#     "last_name": "basit",
#     "age": 20,
#     "city": "sohawa",
# }

# for info in person:
#     print(person[info])

# favourite_numbers = {
#     "alice": 4,
#     "bob": 9,
#     "clark": 21,
#     "stephen": 37,
#     "troy": 55,
# }

# for favourite_number in favourite_numbers:
#     print(
#         f"{favourite_number.title()}'s favourite number is {favourite_numbers[favourite_number]}."
#     )

glossary = {
    "interpreter": "Program that executes code line-by-line without compiling it into a separate executable.",
    "if": "A conditional statement to make decision based on a condition.",
    "for": "A loop that executes a specific number of times based on condition.",
    "while": "A loop that executes as long as a condition remains true.",
    "boolean expression": "An expression that returns either True or False.",
}

for word in glossary:
    print(f"> {word.title()} : {glossary[word]}")
