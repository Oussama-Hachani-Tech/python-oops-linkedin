# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
    def __new__(cls, *args, **kwargs):
        return super(Book, cls).__new__(cls)

    def __init__(self, title):
        self.title = title


# TODO: create instances of the class
quran = Book("Holy Quran")
two_cities = Book("A Tale of Two Cities")

# TODO: print the class and property
print(quran)
print(quran.title)
