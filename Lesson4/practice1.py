# Module 3 part 4
# Example 1 (PZp4)
print("Example 1 (square):")
try:
    size = int(input("enter size of the square (up to 100): "))
    if size > 100:
        raise Exception("Size is greater than 100!")
    if size <= 0:
        raise Exception("Size can't be negative or zero.")
    for i in range(size):
        for j in range(size):
            print("*", end="  ")
        print()
except ValueError as error:
    print("Error: ", error)
except Exception as error:
    print("Error: ", error)

# Example 2 (PZp4)
print("\nExample 2 (rectangle):")
try:
    rows = int(input("enter vertical height of the rectangle: "))
    columns = int(input("enter horizontal length of the rectangle: "))
    if rows > 100 or columns > 100:
        raise Exception("Size is greater than 100!")
    if rows <= 0 or columns <= 0:
        raise Exception("Size can't be negative or zero.")
    for i in range(rows):
        for j in range(columns):
            print("*", end="  ")
        print()
except ValueError as error:
    print("Error", error)
except Exception as error:
    print("Error: ", error)

# Example 3 (PZp4)
print("\nExample 3 (hollow square):")
try:
    size = int(input("enter size of the square (up to 100): "))
    if size > 100:
        raise Exception("Size is greater than 100!")
    if size <= 0:
        raise Exception("Size can't be negative or zero.")
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print("*", end="  ")
            else:
                print(" ", end="  ")
        print()
except ValueError as error:
    print("Error", error)
except Exception as error:
    print("Error: ", error)

# Example 4 (PZp4)
print("\nExample 4 (hollow rectangle):")
try:
    rows = int(input("enter vertical height of the rectangle: "))
    columns = int(input("enter horizontal length of the rectangle: "))
    if rows > 100 or columns > 100:
        raise Exception("Size is greater than 100!")
    if rows <= 0 or columns <= 0:
        raise Exception("Size can't be negative or zero.")
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print("*", end="  ")
            else:
                print(" ", end="  ")
        print()
except ValueError as error:
    print("Error", error)
except Exception as error:
    print("Error: ", error)
