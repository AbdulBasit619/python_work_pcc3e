# car = input("Tell me what car do you like? ")
# print(f"Let me see if I can find you a {car}")

# num_people = int(input("Tell me how many people are there in your group: "))
# if num_people > 8:
#     print("Sorry, you have to wait for a table!")
# else:
#     print("Your table is ready!")

num = int(
    input(
        "Give me a number, and I will tell you whether it is a multiple of 10 or not: "
    )
)
if num % 10 == 0:
    print(f"{num} is a multiple of 10")
else:
    print(f"{num} is not a multiple of 10")
