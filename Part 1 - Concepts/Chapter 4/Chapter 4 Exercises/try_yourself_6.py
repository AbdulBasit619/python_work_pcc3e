# guests = ["Arijit Singh", "Prabhas", "Atif Aslam", "Allu Arjun", "Thalapathy Vijay"]

# print("The first three items in the list are:")
# for guest in guests[:3]:
#     print(guest)

# print("\nThree items from the middle of the list are:")
# for guest in guests[1:-1]:
#     print(guest)

# print("\nThe last three items in the list are:")
# for guest in guests[-3:]:
#     print(guest)

pizzas = ["hot and spicy", "pepperoni", "fajita"]
friend_pizzas = pizzas[:]

pizzas.append("jalapeno")
friend_pizzas.append("vegetarian")

print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
