import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        Circle.count = +1

    def area(self):
        area = self.radius ** 2 * math.pi
        result = f"Area of a circle is {round(area, 2)}."
        return result

    def perimeter(self):
        perimeter = round(self.radius * 2 * math.pi, 2)
        return perimeter

    def __eq__(self, other):
        comparison = self.radius == other.radius
        if comparison:
            result = f"Radius of both objects are equal."
        else:
            result = f"Radius of both objects are different."
        return result

    def __le__(self, other):
        op1 = round(self.radius * 2 * math.pi, 2)
        op2 = round(other.radius * 2 * math.pi, 2)
        result = op1 <= op2
        return result

    def __ge__(self, other):
        op1 = round(self.radius * 2 * math.pi, 2)
        op2 = round(other.radius * 2 * math.pi, 2)
        result = op1 >= op2
        return result

    def __lt__(self, other):
        op1 = round(self.radius * 2 * math.pi, 2)
        op2 = round(other.radius * 2 * math.pi, 2)
        result = op1 < op2
        return result

    def __gt__(self, other):
        op1 = round(self.radius * 2 * math.pi, 2)
        op2 = round(other.radius * 2 * math.pi, 2)
        result = op1 > op2
        return result

    # function for validation
    def compare_per(self, other):
        global result_of_comparison
        op1 = self.radius * 2 * math.pi
        op2 = other.radius * 2 * math.pi
        if op1 > op2:
            result_of_comparison = f"First is greater than second."
        elif op1 < op2:
            result_of_comparison = f"First is less than second."
        elif op1 == op2:
            result_of_comparison = f"Both circles have the same perimeter."

        return result_of_comparison

    def __sub__(self, other):
        reduced1 = self.radius - 1
        reduced2 = other.radius - 1

        per1 = round(reduced1 * 2 * math.pi, 2)
        per2 = round(reduced2 * 2 * math.pi, 2)

        result = f"Radius of the 1st and 2nd circles, after being reduced by 1 are: {reduced1} and {reduced2}." \
                 f"\nNew perimeters are: {per1} and {per2}."
        return result


# create two objects
example1 = Circle(5)
example2 = Circle(6)

# comparing radius of two objects
print("Comparing radius:")
print(f"1st object has radius:", example1.radius)
print(f"2nd object has radius:", example2.radius)
print(example1 == example2)

# comparing perimeter of two objects
print("\nComparing perimeter:")
print("First circle:", example1.perimeter())
print("Second circle:", example2.perimeter())
print(f"First is less than or equal to second:", example1.perimeter() <= example2.perimeter())
print(f"First is greater than or equal to second:", example1.perimeter() >= example2.perimeter())
print(f"First is less than second:", example1.perimeter() < example2.perimeter())
print(f"First is greater than second:", example1.perimeter() > example2.perimeter())

print('\n[checking via regular method]')
print(example1.compare_per(example2))

# proportionate change of perimeters by changing radius (not sure if understood)
print("\nReducing radius of both circles by the same value:")
print(example1 - example2)

