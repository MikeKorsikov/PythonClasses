print("\nExercise 4, conditional update of text:")

try:
    # access data
    with open('given_file.txt', 'r') as file:
        content = file.readlines()
    file.close()

    # identify position of last
    lst_ci = []
    for i in content:
        if ',' not in i:
            lst_ci.append('True')
        else:
            lst_ci.append('False')

    len_of_list = len(lst_ci)
    lst_ci.reverse()
    lst_occ = lst_ci.index('True')
    last_t = len_of_list - lst_occ

    # updating text
    content.insert(last_t, '************\n')
    print(content)

    # record data
    with open('processed_data.txt', 'a') as file2:
        for row in content:
            file2.write(f"{row}")
    file2.close()
    print('Data was successfully processed and saved.')

except Exception as e:
    print(str(e))