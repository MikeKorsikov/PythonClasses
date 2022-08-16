# MODULE 3 part4

# M3p4 - Exercise 1
print("M3p4 - Exercise 1 ")

try:
    first_digit = int(input("Enter first digit in range: "))
    last_digit = int(input("Enter last figure in range: "))

    for num in range(first_digit, last_digit + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
except:
    print("Input positive digits only")

# M3p4 - Exercise 2
print("\nM3p4 - Exercise 2 ")

for i in range(1, 11):
    for j in range(1, 11):
        answer = i * j
        if answer < 10:
            print(i, "*", j, "=", answer, end="    ")
        elif answer >= 10 and answer <= 100:
            print(i, "*", j, "=", answer, end="   ")
        j += 1
    i += 1
    print()

# M3p4 - Exercise 3
print("\nM3p4 - Exercise 3 ")
start = int(input("Enter first digit in range: "))
end = int(input("Enter last figure in range: "))
for i in range(start, end + 1):
    for j in range(1, 11):
        answer = i * j
        if answer < 10:
            print(i, "*", j, "=", answer, end="    ")
        elif answer >= 10 and answer <= 100:
            print(i, "*", j, "=", answer, end="   ")
        j += 1
    i += 1
    print()
