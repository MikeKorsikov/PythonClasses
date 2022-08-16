# MODULE 3 part2

# M3p2 - Exercise 1
print("M3p2 - Exercise 1 ")
first_digit = int(input("Enter first digit in range: "))
last_digit = int(input("Enter last figure in range: ")) + 1
sumOfEven = 0
sumOfOdd = 0
sumOfNines = 0
n_for_even = 0
n_for_odd = 0
n_for_nines = 0

for i in range(first_digit, last_digit):
    if i % 2 == 0:
        sumOfEven += i
        n_for_even += 1
    else:
        sumOfOdd += i
        n_for_odd += 1
    if i % 9 == 0:
        sumOfNines += i
        n_for_nines += 1


avEven = sumOfEven / n_for_even
avOdd = sumOfOdd / n_for_odd
avNines = sumOfNines / n_for_nines

print("\t Sum of even numbers in a range: ", sumOfEven)
print("\t Sum of odd numbers in a range: ", sumOfOdd)
print("\t Sum of multiples of 9 in a range: ", sumOfNines)
print("\n\t Average of even numbers is: ", avEven)
print("\t Average of odd numbers is: ", avOdd)
print("\t Average of numbers multiple of 9 is: ", avNines)

# M3p2 - Exercise 2
print("\nM3p2 - Exercise 2 ")
length = int(input("Enter length of line (in digits): "))
type_of_symbol = input("Enter symbol to display: ")
i = 1

while i < length+1:
    print(type_of_symbol, end="\n")
    i += 1

# M3p2 - Exercise 3
print("\nM3p2 - Exercise 3 ")

while True:
    digit = int(input("\nPlease enter number: "))
    if digit > 0:
        print("\tNumber is positive.")
    elif digit < 0:
        print("\tNumber is negative.")
    else:
        print("\tNumber is equal to zero.")
    if digit == 7:
        print("\tGood bye!")
        break

# M3p2 - Exercise 4
print("\nM3p2 - Exercise 4 ")
maxNumber = 1
minNumber = 1
sumOfNumbers = 0
breakTrigger = 7

while True:
    digit = int(input("\nPlease enter number: "))
    sumOfNumbers += digit

    if digit > maxNumber:
        maxNumber = digit
    if digit < minNumber:
        minNumber = digit

    if digit == breakTrigger:
        print("\tGood bye!")
        print("\tSum of digits entered:", sumOfNumbers)
        print("\tMaximum number was: ", maxNumber)
        print("\tMinimum number was: ", minNumber)
        break
