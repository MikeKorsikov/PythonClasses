# HW on abstract factory (to create a family of related objects)

class CourseAtITStep:
    def __init__(self, courses_factory=None):
        self.course_factory = courses_factory

    def show_details(self):
        course = self.course_factory()
        print("We have a course named {course}.".format(course=course))
        print("its price is {fee}.".format(fee=course.fee()))


class Python:
    def fee(self):
        price = 40000
        return price

    def __str__(self):
        return "Python course for beginners"


class WebDesign:
    def fee(self):
        price = 35000
        return price

    def __str__(self):
        return "Web design for beginners"


class Crypto:
    def fee(self):
        price = 50000
        return price

    def __str__(self):
        return 'Blockchain and crypto technologies (advanced)'


#
course = CourseAtITStep(Python)
course.show_details()
