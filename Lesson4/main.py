# Exceptions
# https://docs.python.org/3/library/exceptions.html

# Example 1
# print("\n Example 1")
# number = "5z"
# num = int(number)
# print(num)
# print('Hello')

# error handler
try:
    number = "5z"
    num = int(number)
    print(num)
except:
    print("Type error")
print("Continue working...")

# Example 2
print("\n Example 2")

try:
    # code which might lead to error
    number = int(input("Enter number: "))
    print("Number:", number)
except:
    print("Error in value!")
finally:
    print("End of this block")
print("Continue...")


# Example 3
print("\n Example 3 (with standard error description")
try:
    # other error
    number = int(input("Enter number: "))
    print("Number:", number)
except ValueError as error:
    print("ValueError:", error)
except:
    print("Other error!")

# Example 4
print("\n Example 4")
try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    print("Division:", int(num1 / num2))
except ValueError as error:
    print("Error:", error)
except ZeroDivisionError as error:
    print("Error:", error)
except BaseException as error:
    print("Error:", error)
except:
    print("Error!")

# Example 5
print("\n Example 5")
try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    print("Division:", num1 / num2)
except (ValueError, ZeroDivisionError):
    print("Error in value or division by zero.")

# Example 6
print("\n Example 6")
try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    if num2 == 0:
        raise Exception("Second number is zero!")
    print("Division:", num1/num2)
except ValueError as error:
    print("Error", error)
except Exception as error:
    print("Error", error)