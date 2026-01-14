# sandwich_orders = [
#     "BLT",
#     "Club",
#     "pastrami",
#     "Peanut Butter",
#     "pastrami",
#     "Cheese",
#     "Cuban",
#     "pastrami",
# ]

# finished_sandwiches = []

# print("The deli has run out of pastrami!")
# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")

# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print(f"I made your {sandwich} sandwich!")
#     finished_sandwiches.append(sandwich)

# while finished_sandwiches:
#     print(f"{finished_sandwiches.pop()} sandwich was made.")

dream_locations = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    dream_locations[name] = response

    repeat = input("Do you want other users to respond as well? (yes, no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll results ---")
for name, response in dream_locations.items():
    print(f"{name.title()}'s dream location is {response.title()}")
