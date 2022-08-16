import string
import random

# Cycles

# Example 1
print("\n Example 1")
for i in range(10):
    print(i)

nums = range(10)  # to
print(nums)

nums = range(2, 8)  # from, to
print(nums)

nums = range(0, 10, 2)  # from, to, step
print(nums)

# Example 2 (cartage)
print("\n Example 2")
for i in 1, 4, 2, 6, 2:
    print(i)

# Example 3 (string as a collection)
print("\n Example 3")
name = 'Vasya'
for i in name:
    print(i)

# Example 4 (string as a collection)
print("\n Example 4")

name = 'Vasya'
for i in name:
    print(i)
    break
else:
    print('end')

# Example 5
print("\n Example 5")

i = 1
j = 1

while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1

# Example 6
print("\n Example 6")

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1

# Example 7 (generate password)
print("\n Example 7")

numbers = string.digits
letters = string.ascii_letters
symbols = string.punctuation

password_data = numbers + letters + symbols
print(password_data)

password = ""

for i in range(12):
    symbol = random.choice(password_data)
    password += symbol
print("New password: ", password)

# Example 8 (generate password)
print("\n Example 8")

numbers = string.digits
letters = string.ascii_letters
symbols = string.punctuation
password_data = numbers + letters + symbols
print(password_data)

password = ""

while True:
    choice = input("Enter 'q' for exit, enter anything to continue: ")
    if choice == 'q':
        print("Exit!")
        break

    while True:
        pass_length = int(input("Enter password length: "))
        if pass_length >= 8 and pass_length <= 16:
            for i in range(pass_length):
                symbol = random.choice(password_data)
                password += symbol
            print("New password: ", password)
            password = ""
            break
        else:
            print("Incorrect length")



