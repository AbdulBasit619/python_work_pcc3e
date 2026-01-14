# """Implementing an addition program for the purposes of Exception Handling."""

# a = input("Enter the first number: ")
# b = input("Enter the second number: ")

# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     print("Both inputs must be a valid number!")
# else:
#     sum = a + b
#     print(f"The sum of {a} and {b} is {sum}.")


# """Implementing an addition calculator for the purposes of Exception Handling."""

# print("Enter two number, and I will tell you their sum: ")
# print("Enter 'q' to quit")
# while True:
#     a = input("\nEnter the first number: ")
#     if a == "q":
#         break

#     b = input("Enter the second number: ")
#     if b == "q":
#         break

#     try:
#         a = int(a)
#         b = int(b)
#     except ValueError:
#         print("Both inputs must be a valid number!")
#     else:
#         sum = a + b
#         print(f"The sum of {a} and {b} is {sum}.")

# from pathlib import Path

# cats = Path("cats.txt")
# dogs = Path("dogs.txt")

# try:
#     cats_contents = cats.read_text()
#     dogs_contents = dogs.read_text()
# except FileNotFoundError:
#     print("Some files were not found in this path!")
# else:
#     print(cats_contents)
#     print(dogs_contents)

# try:
#     cats_contents = cats.read_text()
#     dogs_contents = dogs.read_text()
# except FileNotFoundError:
#     pass
# else:
#     print(cats_contents)
#     print(dogs_contents)
