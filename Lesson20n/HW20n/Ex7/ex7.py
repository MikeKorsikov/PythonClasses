print('Exercise 7:')

given_list = ['row1', 'row2', 'row3']

try:
    for i in given_list:
        file = open('destination.txt', 'a')
        file.write(f'{i}\n')
        file.close()

except Exception as e:
    print(str(e))
