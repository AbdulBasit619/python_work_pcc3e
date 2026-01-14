from pathlib import Path

# path = Path("guest.txt")
# name = input("What is your name? ")
# path.write_text(name)

path = Path("guest_book.txt")

prompt = "\nWhat is your name? (press q to quit) "

names = []

active = True
while active:
    name = input(prompt)
    if name == "q":
        active = False
    else:
        names.append(name)

output = ""
for name in names:
    output += f"{name}\n"

path.write_text(output)
