#Exercise 1 (warm up)
print("\nExercise 1 ")
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

if first > second and first > third:
    print("Number ", first, " is greatest.")
elif second > first and second > third:
    print("Number ", + second, " is greatest.")
else:
    print("Number ", third, " is greatest.")

#Exercise 2 (warm up)
print("\nExercise 2 ")
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

if first == second and first == third:
    print("All 3 are equal.")
elif first == second or first == third:
    print("Only two are equal")
else:
    print("All numbers are unique")

#Exercise 1 (Practice)
print("\nExercise 1 ")
digit = int(input("Enter number to check if even or odd: "))

if digit % 2 == 0:
    print(digit, "is Even.")
else:
    print(digit, "is Odd.")

#Exercise 2 (Practice)
print("\nExercise 2 ")
multiple = 7
digit = int(input("Enter number to check if multiple of 7: "))

if digit % 7 == 0:
    print(digit, "is multiple of 7.")
else:
    print(digit, "is NOT multiple of 7.")

# Exercise 3 (Practice)
print("\nExercise 3 ")
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if first > second:
    print(first, "is greater.")
elif second > first:
    print(second, "is greater.")
else:
    print("Numbers are equal.")

# Exercise 4 (Practice)
print("\nExercise 4 ")
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if first < second:
    print(first, "is smaller.")
elif second < first:
    print(second, "is smaller.")
else:
    print("Numbers are equal.")

# Exercise 5 (Practice)
print("\nExercise 5 ")
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
operator = int(input("Enter operator:\n 1 - addition \n 2 - deduction \n 3 - average \n 4 - multiplication \n\t Choice:"))

answer = 0

if operator == 1:
    answer = first + second
    print("Answer is: ", answer)
elif operator == 2:
    answer = first - second
    print("Answer is: ", answer)
elif operator == 3:
    answer = ((first + second)/2)
    print("Answer is: ", answer)
else:
    answer = first * second
    print("Answer is: ", answer)


