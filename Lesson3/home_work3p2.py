# MODULE 3 part5

# M3p4 - Exercise A
print("M3p5 - Exercise A (1 upper right)")
upper_limit = 3

i = upper_limit
while i >= 1:
    j = upper_limit
    while j > i:
        print('  ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('* ', end=' ')
        k += 1
    print()
    i -= 1

# M3p4 - Exercise B
print("\nM3p5 - Exercise B (2 lower left)")
upper_limit = 3

for i in range(0, upper_limit):
    for j in range(0, i + 1):
        print('*  ', end='')
    print('\r')

# M3p4 - Exercise C
print("\nM3p5 - Exercise C (3 pyramid facing down)")
upper_limit = 3
for i in range(upper_limit):
    for j in range(i):
        print('  ', end='')
    for j in range(2*(upper_limit-i)-1):
        print('* ', end='')
    print()

# M3p4 - Exercise D
print("\nM3p5 - Exercise D (4 pyramid facing up)")
k = upper_limit - 1

for i in range(0, upper_limit):
    for j in range(0, k):
        print(end='  ')
    k = k - 1
    for j in range(0, i + 1):
        print('*   ', end='')
    print('\r')

# M3p4 - Exercise E
print("\nM3p5 - Exercise E (5 vertical sand-watch)")
upper_limit = 3

for i in range(upper_limit, 0, -1):
    for j in range(upper_limit - i):
        print(' ', end=' ')
    for j in range(1, 2 * i):
        print('* ', end='')
    print()

for i in range(2, upper_limit + 1):
    for j in range(upper_limit - i):
        print(' ', end=' ')
    for j in range(1, 2 * i):
        print('* ', end='')
    print()

# M3p4 - Exercise F
print("\nM3p5 - Exercise F (6 vertical sand-watch)")

# M3p4 - Exercise G
print("\nM3p5 - Exercise G (7 pyramid facing right)")
upper_limit = 3
for i in range(0, upper_limit):
    for j in range(0, i + 1):
        print('* ', end=' ')
    print('\r')

for i in range(upper_limit, 0, -1):
    for j in range(0, i - 1):
        print('* ', end=' ')
    print('\r')


# M3p4 - Exercise H
print("\nM3p5 - Exercise H (8 pyramid facing left)")
upper_limit = 3
i = 1
while i <= upper_limit:
    j = i
    while j < upper_limit:
        print('   ', end='')
        j += 1
    k = 1
    while k <= i:
        print('*  ', end='')
        k += 1
    print()
    i += 1

i = upper_limit
while i >= 1:
    j = i
    while j <= upper_limit:
        print('   ', end='')
        j += 1
    k = 1
    while k < i:
        print('*  ', end='')
        k += 1
    print('')
    i -= 1


# M3p4 - Exercise I
print("\nM3p5 - Exercise I (9 upper left)")
upper_limit = 3

for i in range(upper_limit + 1, 0, -1):
    for j in range(0, i - 1):
        print('*  ', end='')
    print(' ')

# M3p4 - Exercise J
print("\nM3p5 - Exercise J (10 lower right)")
upper_limit = 3
k = upper_limit + 1

for i in range(upper_limit):
    for j in range(1, upper_limit - i):
        print('   ', end='')
    for k in range(i + 1):
        print('*  ', end='')
    print('\r')
