print('Exercise 1: ')

lines = []
bad_words = ['говнюк', 'жлоб', 'блатнюк']

try:
    with open('text.txt', 'r') as f:
        if f.readable():

            lines = ' '.join(list(
                filter(lambda x: x.replace('\n', ' ') not in bad_words, ' '.join(
                    list(map(lambda x: x, f.readlines()))).split(" "))))
            print(lines)

    with open('text2.txt', 'w') as f2:
        if f2.writable():
            f2.writelines(lines)
except Exception as e:
    print("Can't open fie " + str(e))



