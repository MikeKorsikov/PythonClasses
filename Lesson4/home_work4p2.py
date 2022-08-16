import sys
import time

# MODULE 4 part2

# M4p2 - Exercise 1
print("M4p2 - Exercise 1 (calculator)")
symbols = ['+', '-', '*', '/']
expr_spl = []
running = True
while running:
    start = input("Initiate calculator [Y/N]: ")
    if start.lower() == 'n':
        print("Process is terminated. ")
        running = False
        break
    elif start.lower() == 'y':
        running = False
        print("\nInitiating calculator", end="")
        for i in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.3)
        expression = input("\n\nEnter single arithmetic expression using +, -, *, / : ")
        expression = str(expression)
        for i in expression:
            if i in symbols:
                symb_ind = expression.find(i)
                first_digit = expression[0:symb_ind]
                symb = expression[symb_ind]
                second_digit = expression[symb_ind+1:len(expression)]

                expr_spl.append(first_digit)
                expr_spl.append(symb)
                expr_spl.append(second_digit)

        if expr_spl[1] == "+":
            result = int(expr_spl[0]) + int(expr_spl[2])
            print(f"{expression}={result}")
        elif expr_spl[1] == "-":
            result = int(expr_spl[0]) - int(expr_spl[2])
            print(f"{expression}={result}")
        elif expr_spl[1] == "*":
            result = int(expr_spl[0]) * int(expr_spl[2])
            print(f"{expression}={result}")
        elif expr_spl[1] == "/":
            result = int(expr_spl[0]) / int(expr_spl[2])
            print(f"{expression}={result}")

    else:
        print("Enter Y or N")

# M4p2 - Exercise 2
print("\nM4p2 - Exercise 2")
list_of_num = [100, 1, 2, 3, 0, -1, -2, -5, 0, 0, 1000, -1000]
smalles_num = min(list_of_num)
largest_num = max(list_of_num)
num_of_pos = 0
num_of_neg = 0
num_of_zer = 0

for i in list_of_num:
    if i > 0:
        num_of_pos += 1
    elif i < 0:
        num_of_neg += 1
    elif i == 0:
        num_of_zer += 1

print(f"In a list {list_of_num}:")
print(f"\nSmallest number is: {smalles_num}")
print(f"Largest number is: {largest_num}")
print(f"Number of negative digits is: {num_of_neg}")
print(f"Number of positive digits is: {num_of_pos}")
print(f"Number of zeroes is: {num_of_zer}")