print('\nExercise 2 Statistics of text in the given file:')

try:

    # count symbols
    oldfile = open('oldfile.txt', 'r')
    num_of_symb = len(oldfile.read())
    print(f'Number of symbols: {num_of_symb}')
    oldfile.close()

    # count rows
    oldfile = open('oldfile.txt', 'r')
    num_of_rows = oldfile.readlines()
    count_rows = 0
    for i in num_of_rows:
        count_rows += 1
    print(f'Number of rows: {count_rows}')
    oldfile.close()

    # count number of vowels
    voweles = ('a', 'e', 'i', 'o', 'u', 'y')
    oldfile = open('oldfile.txt', 'r')

    list_of_symb = []
    count_vowels = 0
    for i in oldfile.read():
        list_of_symb.append(i)
    for i in list_of_symb:
        if i in voweles:
            count_vowels += 1
    print(f'Number of vowels: {count_vowels}')
    oldfile.close()

    # count consonants
    consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                  'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')
    oldfile = open('oldfile.txt', 'r')

    list_of_symb = []
    count_consonants = 0
    for i in oldfile.read():
        list_of_symb.append(i)
    for i in list_of_symb:
        if i in consonants:
            count_consonants += 1
    print(f'Number of consonants: {count_consonants}')
    oldfile.close()

    # count number of digits
    digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    oldfile = open('oldfile.txt', 'r')

    list_of_symb = []
    count_digits = 0
    for i in oldfile.read():
        list_of_symb.append(i)
    for i in list_of_symb:
        try:
            dig_i = int(i)
            if dig_i in digits:
                count_digits += 1
        except Exception:
            pass
    print(f'Number of digits: {count_digits}')
    oldfile.close()

    # create new file
    newfile = open('newfile.txt', 'w')
    text_to_be_added = [f"Number of symbols: {num_of_symb} "
                        f"\nNumber of rows: {count_rows} "
                        f"\nNumber of vowels: {count_vowels} "
                        f"\nNumber of consonants: {count_consonants}"
                        f"\nNumber of digits: {count_digits}"]

    newfile.writelines(text_to_be_added)
    newfile.close()
    print('\nNew file is generated.')

except Exception as e:
    print(str(e))
