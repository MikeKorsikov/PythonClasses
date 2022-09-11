# Decorator goes first


def methodDecorator(method_to_decorate):
    def wrapper(self):
        print("General information:")
        method_to_decorate(self)
    return wrapper


# Class goes second
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    @methodDecorator
    def showInfo(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Pages: {}".format(self.pages))


# Creation of object goes third
book1 = Book("Python Crash Course", "Eric Matthes", 624)

# Invoking function goes last
book1.showInfo()
