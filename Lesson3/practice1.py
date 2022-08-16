# Example 1 (PZ)
print("Example 1 (print range)")

first_digit = int(input("Enter first digit in range: "))
last_digit = int(input("Enter last figure in range: ")) + 1

for i in range(first_digit, last_digit):
    print(i)
    i += 1

# Example 2 (PZ)
print("\n Example 2 (odd numbers)")
first_digit = int(input("Enter first digit in range: "))
last_digit = int(input("Enter last figure in range: ")) + 1

for i in range(first_digit, last_digit):
    if i % 2 != 0:
        print(i)
    i += 1

# Example 3 (PZ)
print("\n Example 3 (even numbers)")
first_digit = int(input("Enter first digit in range: "))
last_digit = int(input("Enter last figure in range: ")) + 1

for i in range(first_digit, last_digit):
    if i % 2 == 0:
        print(i)
    i += 1

# Example 4 (PZ)
print("\n Example 4 (reverse order)")
first_digit = int(input("Enter first digit in range: ")) - 1
last_digit = int(input("Enter last figure in range: "))

for i in range(first_digit, last_digit):
    i = last_digit
    print(i)
    last_digit -= 1

# Example 5 (PZ)
print("\n Example 5 (data normalisation)")
first_digit = int(input("Enter first digit in range: "))
last_digit = int(input("Enter last figure in range: ")) + 1

if first_digit > last_digit:
    new_first = last_digit - 1
    new_last = first_digit
    for i in range(new_first, new_last):
        if i % 2 != 0:
            print(i)
        i += 1
else:
    for i in range(first_digit, last_digit):
        if i % 2 != 0:
            print(i)
        i += 1