import math

# Exercise 1 (Practice#2)
print("\nExercise 1 ")
seconds_input = int(input("Enter number of seconds: "))
time_period = int(input("Enter time period: \n 1 - seconds \n 2 - minutes \n 3 - hours \n\t Choice: "))

# Seconds in each time period
second = 1
minute = second * 60
hour = minute * 60
day = hour * 24

remainder_seconds = day - seconds_input
remainder_minutes = remainder_seconds / 60
remainder_hours = remainder_minutes / 60

if time_period == 1:
    print("Till midnight: ", remainder_seconds, "seconds.")
elif time_period == 2:
    print("Till midnight: ", remainder_minutes, "minutes.")
elif time_period == 3:
    print("Till midnight: ", remainder_hours, "hours.")
else:
    print("Choice out of range")

# Exercise 2 (Practice#2)
print("\nExercise 2 ")
diameter = int(input("Enter diameter of circle: "))
choice = int(input("do you want to calculate: \n 1 - area \n 2 - perimeter \n\t Choice: "))
radius = diameter / 2

if choice == 1:
    area = math.pi * radius ** 2
    print("Area of circle is equal to: ", area)
elif choice == 2:
    perimeter = 2 * math.pi * radius
    print("Perimeter of circle is equal to: ", perimeter)
else:
    print("Choice out of range.")

# Exercise 3 (Practice#2)
print("\nExercise 3")
price = int(input("Enter price of one console: "))
quantity = int(input("Enter quantity: "))
discount = int(input("Enter discount in % (e.g. 5): "))

total_price = price * quantity * (1-discount/100)

print("Total price is ", total_price)
