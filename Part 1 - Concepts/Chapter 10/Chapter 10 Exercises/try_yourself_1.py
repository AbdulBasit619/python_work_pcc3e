from pathlib import Path

path = Path("learning_python.txt")

contents = path.read_text()
# print(contents)

# lines = contents.splitlines()

# print("\n")
# for line in lines:
#     print(line)

for line in contents.splitlines():
    print(line)

c_lines = contents.replace("Python", "C")
print(c_lines)
