# Создайте программу «Книжная коллекция». Нужно
# хранить информацию о книгах: автор, название книги,
# жанр, год выпуска, количество страниц, издательство.
# Требуется реализовать возможность добавления, удаления, поиска,
# замены данных. Используйте словарь для
# хранения информации.

library = []


def menu():
    print("1. Add book\n2. Remove book\n3. Search book by\n4. Exit\n5. Show Books")
    while True:
        try:
            return int(input("Enter choose: "))
        except ValueError as e:
            print("Error: " + str(e) + "\nENTER VALID OPTION\n")
        except BaseException as e:
            print("Error: " + str(e))


def add_book():
    book = {}

    author = input("Enter author name:")
    if author.isalpha() and len(author) < 50:
        book["author"] = author

    book_t = input("Enter book title:")
    if len(book_t) < 50:
        book["book title"] = book_t

    genre = input("Enter genre name:")
    if genre.isalpha() and len(genre) < 50:
        book["genre"] = genre

    while True:
        try:
            year = int(input("Enter year:"))
            if year >= 0:
                book["year"] = year
                break
        except ValueError as e:
            print("Error: " + str(e) + "\nENTER VALID YEAR\n")
        except BaseException as e:
            print("Error: " + str(e))

    while True:
        try:
            pages = int(input("Enter pages count:"))
            if pages > 0:
                book["pages"] = pages
                break
        except ValueError as e:
            print("Error: " + str(e) + "\nENTER VALID PAGES COUNT\n")
        except BaseException as e:
            print("Error: " + str(e))

    publisher = input("Enter publisher name:")
    if len(publisher) < 50:
        book["publisher"] = publisher

    return book


def search_book():
    global library
    founds_book = []
    filds = {1: "author", 2: "book title", 3: "genre", 4: "year", 5: "pages", 6: "publisher"}
    print("Enter criteria for search\n"
          "1. Author\n2. Book Title\n3. Genre\n4. Year\n5. Pages Count\n6. Publisher")
    while True:
        try:
            answer = int(input("Enter choose: "))
            if answer == 4 or answer == 5:
                search = int(input("Enter number to search: "))
            else:
                search = input("Enter word to search: ")

            if answer in filds:
                selected = filds[answer]
                for i in library:
                    for key, val in i.items():
                        if selected == key and val == search:
                            founds_book.append(i)
            break
        except ValueError as e:
            print("Error: " + str(e) + "\nENTER VALID OPTION\n")
        except BaseException as e:
            print("Error: " + str(e))

    return founds_book


def show_book(book):
    for key, val in book.items():
        print(f"{key.title()} - {val}")


def remove_book():
    global library
    print("Remove book")
    book = search_book()
    if len(book) > 0:
        for i in library:
            for j in book:
                if i == j:
                    ind = library.index(i)
                    del library[ind]


answer = 0
while answer != 4:
    answer = menu()
    if answer == 1:
        library.append(add_book())
    elif answer == 2:
        remove_book()
    elif answer == 3:
        ls = search_book()
        if len(ls) != 0:
            for i in ls:
                show_book(i)

    elif answer == 5:
        if len(library) > 0:
            for i in library:
                show_book(i)
        else:
            print("Lib empty")
