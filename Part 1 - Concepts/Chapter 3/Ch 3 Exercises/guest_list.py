guests = ["Arijit Singh", "Prabhas", "Atif Aslam"]
print(f"Dear {guests[0]}, it would be a pleasure to have you for dinner.")
print(f"Dear {guests[0]}, it would be a pleasure to have you for dinner.")
print(f"Dear {guests[2]}, it would be a pleasure to have you for dinner.")

print(f"{guests[2]} could not make it to dinner.")

guests[2] = "Fahad Mustafa"

print(f"Dear {guests[0]}, it would be a pleasure to have you for dinner.")
print(f"Dear {guests[1]}, it would be a pleasure to have you for dinner.")
print(f"Dear {guests[2]}, it would be a pleasure to have you for dinner.")

print("Dear guests, I found a bigger table.")

guests.insert(0, "Allu Arjun")
guests.insert(2, "Shahrukh Khan")
guests.append("Elon Musk")

print(f"Dear {guests[0]}, it would be a pleasure to have you for dinner.")
print(f"Dear {guests[1]}, it would be a pleasure to have you for dinner.")
print(f"Dear {guests[2]}, it would be a pleasure to have you for dinner.")
print(f"Dear {guests[3]}, it would be a pleasure to have you for dinner.")
print(f"Dear {guests[4]}, it would be a pleasure to have you for dinner.")

print("Respected guests, I am so sorry that a bigger table would not be available in time for all the guests to sit. I will have space for only two guests.")
guest_1 = guests.pop()
guest_2 = guests.pop()
guest_3 = guests.pop()
guest_4 = guests.pop()

print(f"It is with great sorrow that you, {guest_1}, are no longer invited for dinner.")
print(f"It is with great sorrow that you, {guest_2}, are no longer invited for dinner.")
print(f"It is with great sorrow that you, {guest_3}, are no longer invited for dinner.")
print(f"It is with great sorrow that you, {guest_4}, are no longer invited for dinner.")

print(f"Dear {guests[0]}, it would be a pleasure to have you for dinner.")
print(f"Dear {guests[1]}, it would be a pleasure to have you for dinner.")

del guests[0]
del guests[0]
print(guests)