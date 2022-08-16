import random

# PART 3
print("Exercise 1:")



print('\nExercise 2:')
threeDigitNumber = random.randint(1, 999)
first = threeDigitNumber // 100
# second = threeDigitNumber // 10 % 10
second = threeDigitNumber % 100 // 10
third = threeDigitNumber % 10

print("Random number is: ",threeDigitNumber)
print('\nFirst digit is: ', first, '\nSecond digit is: ', second, '\nThird digit is: ', third)
print('Sum of three digits is: ', first + second + third)
