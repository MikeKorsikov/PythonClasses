# MODULE 3 part1

# M3 - Exercise 1
print("M3p1 - Exercise 1 ")
first_digit = int(input("Enter first digit in range: "))
last_digit = int(input("Enter last figure in range: ")) + 1
print("Multiple of 7 in the range are: ")
for i in range(first_digit, last_digit):
    if i % 7 == 0:
        print(i)

# M3 - Exercise 2
print("\nM3p1 - Exercise 2 ")
first_digit = int(input("Enter first number in range: "))
last_digit = int(input("Enter last number in range: "))

print("\n 2.1 display all numbers in a range")
for i in range(first_digit, last_digit+1):
    print(i)

print("\n # 2.2 display all numbers in reverse order")
for i in range(last_digit, first_digit-1, -1):
    print(i)


print("\n # 2.3 display all multiples of 7")
print("Multiple of 7 in the range are: ")
for seven in range(first_digit, last_digit+1):
    if seven % 7 == 0:
        print(seven)

print("\n # 2.4 display number of multiples of 5")
counter_for_five = 0
for i in range(first_digit, last_digit+1):
    if i % 5 == 0:
        counter_for_five += 1
print("There are", counter_for_five, "multiples of 5.")

# M3 - Exercise 3
print("\nM3p1 - Exercise 3 ")
first_digit = int(input("Enter first number in range: "))
last_digit = int(input("Enter last number in range: "))

for i in range(first_digit, last_digit+1):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    if i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    if i % 3 != 0 and i % 5 != 0:
        print(i)
