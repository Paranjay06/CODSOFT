import random
import string

print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

length = int(input("Enter password length: "))

print("\nChoose Password Complexity:")
print("1. Letters Only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    characters = string.ascii_letters
elif choice == "2":
    characters = string.ascii_letters + string.digits
elif choice == "3":
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice!")
    exit()

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)