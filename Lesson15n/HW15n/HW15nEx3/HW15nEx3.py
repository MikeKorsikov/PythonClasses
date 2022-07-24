print('\nExercise 3 Removing last row:')

try:
    # process source file
    sourcefile = open('sourcefile.txt', 'r')
    list_of_rows = sourcefile.readlines()
    sourcefile.close()

    # process destination file
    destinationfile = open('destinationfile.txt', 'w')
    n = len(list_of_rows)
    i = 0

    for row in list_of_rows:
        if i < n-1:
            destinationfile.write(row)
        i += 1
    destinationfile.close()

    # Display content of both files
    sourcefile = open('sourcefile.txt', 'r')
    destinationfile = open('destinationfile.txt', 'r')
    list_of_rows2 = destinationfile.readlines()

    print(f'List of rows in source file: {list_of_rows}')
    print(f'List of rows in destination file: {list_of_rows2}')

except Exception as e:
    print(str(e))
