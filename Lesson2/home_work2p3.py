# MODULE 3 part3

# M3p3 - Exercise 1
print("M3p3 - Exercise 1 ")

while True:
    print("//  To quite, enter [0]  //")
    base_digit = int(input("\nEnter base: "))
    if base_digit == 0:
        print("Good bye!")
        break
    else:
        power_digit = int(input("Enter power: "))
        result = base_digit ** power_digit
        print(base_digit, "to the power of", power_digit, "is equal to", result)

# M3p3 - Exercise 2
print("\nM3p3 - Exercise 2 ")

range_start = 100
range_end = 999
counter_of_ident = 0

for i in range(range_start, range_end+1):
    first_digit = i // 100
    second_digit = i % 100 // 10
    third_digit = i % 10
    if first_digit == second_digit or first_digit == third_digit:
        counter_of_ident += 1
    elif second_digit == third_digit:
        counter_of_ident += 1
    else:
        continue

print("In a range from", range_start, "to", range_end, "there are:")
print(counter_of_ident,"numbers which have 2 identical digits in them.")

# M3p3 - Exercise 3
print("\nM3p3 - Exercise 3 ")
range_start = 100
range_end = 9999
counter_of_uniq = 0

for i in range(range_start, range_end + 1):
    if len(str(i)) == 4:
        first_digit = i // 1000
        second_digit = i % 1000 // 100
        third_digit = i % 100 // 10
        fourth_digit = i % 10

        if first_digit != second_digit \
                and first_digit != third_digit \
                and first_digit != fourth_digit \
                and second_digit != third_digit \
                and second_digit != fourth_digit \
                and third_digit != fourth_digit:
            counter_of_uniq += 1
        else:
            continue

    elif len(str(i)) == 3:
        first_digit = i // 100
        second_digit = i % 100 // 10
        third_digit = i % 10

        if first_digit != second_digit \
                and first_digit != third_digit \
                and second_digit != third_digit:
            counter_of_uniq += 1
        else:
            continue

print("In a range from", range_start, "to", range_end, "there are")
print(counter_of_uniq,"numbers which have different digits (e.g. 1234).")

# M3p3 - Exercise 4
print("\nM3p3 - Exercise 4 ")

base_digit = int(input("\nEnter number: "))
