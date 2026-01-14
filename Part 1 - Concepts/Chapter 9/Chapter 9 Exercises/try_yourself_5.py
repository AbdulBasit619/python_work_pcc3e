# from random import randint
from random import sample

# class Die:
#     """An attempt to simulate a rolling die."""

#     def __init__(self, sides=6):
#         self.sides = sides

#     def roll_die(self):
#         print(randint(1, self.sides))


# die_with_6_sides = Die()

# for i in range(1, 11):
#     die_with_6_sides.roll_die()

# die_with_10_sides = Die(10)
# for i in range(1, 11):
#     die_with_10_sides.roll_die()

# die_with_20_sides = Die(20)
# for i in range(1, 11):
#     die_with_20_sides.roll_die()

items = [8, 15, 22, 27, 31, 49, 52, 56, 64, 78, 90, "A", "E", "I", "O", "U"]

print(
    f"Any ticket that matches these 4 numbers or letters wins a prize: {sample(items,4)}"
)

my_ticket = [31, "A", "U", 15]

attempts = 0

while True:
    attempts += 1
    winning_ticket = sample(items, 4)

    if winning_ticket == my_ticket:
        break


print(attempts)
