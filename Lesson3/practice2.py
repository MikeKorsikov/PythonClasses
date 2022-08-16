# Example 1 (PZ_2)
print("Example 1 (sum of numbers in a range + average)")

first_digit = int(input("Enter first digit in range: "))
last_digit = int(input("Enter last figure in range: "))
sum_of_digits = 0
number_of_digits = 0

for i in range(first_digit, last_digit+1):
    sum_of_digits = sum_of_digits + i
    number_of_digits += 1
    i += 1

print("Sum of numbers in a range: ", sum_of_digits)
average_in_range = sum_of_digits / number_of_digits
print("The average is: ", average_in_range)

# Example 2 (PZ_2)
print("\nExample 2 (factorial)")
number = int(input("Enter a number: "))
factorial_result = 1

for i in range(1, number + 1):
    factorial_result = factorial_result * i
print("The factorial of", number, "is", factorial_result)

# Example 3 (PZ_2)
print("\n Example 3 (*-line)")

length = int(input("Enter length of line (in digits): "))
i = 1

while i < length+1:
    print("*", end="")
    i += 1

# Example 4 (PZ_2)
print("\n\n Example 4 (line and symbol)")
length = int(input("Enter length of line (in digits): "))
type_of_symbol = input("Enter symbol to display: ")
i = 1

while i < length+1:
    print(type_of_symbol, end="")
    i += 1