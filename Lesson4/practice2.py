import random

# Module 3 part5
# Example 1 (PZm3p5)
print("\nExample 1 (F@cking with the number):")
try:
    digit = int(input("Enter a number (up to a 9,999): "))
    if digit > 9999:
        raise Exception("Number is greater than a 9,999!")
    if digit < 0:
        raise Exception("Number can't be negative.")
    if digit == 0:
        raise Exception("Number can't be zero.")

    # code itself

    length = len(str(digit))
    print("\n1.1. The length of the number is:", length)

    first_digit = digit // 1000
    second_digit = digit % 1000 // 100
    third_digit = digit % 100 // 10
    fourth_digit = digit % 10
    sum_of_digits = first_digit + second_digit + third_digit + fourth_digit
    print("1.2. The sum of digits is =", sum_of_digits)

    average = sum_of_digits / length
    print("1.3. The average of the numbers is:", average)

    zeros = str(digit).count('0')
    if zeros == 0:
        print("1.4. There are no zeros in the number", digit)
    elif zeros == 1:
        print("1.4. There is only 1 zero in the number", digit)
    else:
        print("1.4. There are", zeros, "zeros in the number", digit)

except ValueError as error:
    print("Error: ", error)
except Exception as error:
    print("Error: ", error)

# Example 2 (PZm3p5)
print("\nExample 2 (chess board):")
try:
    board_size = 3
    square = int(input("enter size of the square (between 1 and 5): "))
    if square > 5:
        raise Exception("Size is greater than 5!")
    if square <= 1:
        raise Exception("Size can't be negative or one.")

    # CODE

except ValueError as error:
    print("Error", error)
except Exception as error:
    print("Error: ", error)

# Example 3 (PZm3p5)
print("\nExample 3 (multiplication):")
try:
    count_positive = 0
    count_negative = 0
    max_tries = 5

    for i in range(max_tries):
        first_number = random.randint(1, 9)
        second_number = random.randint(1,9)
        print("\n", first_number, "*", second_number, "=")
        result = first_number * second_number
        guess = int(input("Your guess: "))
        if guess > 100:
            raise Exception("Answer is greater than a 100!")
        if guess < 0:
            raise Exception("Answer can't be negative.")
        if guess == 0:
            raise Exception("Answer can't be zero.")

        if guess == result:
            print("Well done")
            count_positive += 1
        else:
            print("Wrong anwser")
            count_negative += 1

    score = int(count_positive / max_tries * 100)
    print("Your score is:", score, "percent out of 100.")


except ValueError as error:
    print("Error", error)
except Exception as error:
    print("Error: ", error)

