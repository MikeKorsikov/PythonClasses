# files
print('Exercise 1 - Check if rows of two files are identical:\n')
try:
    file1 = open('file1.txt', 'r')
    file2 = open('file2.txt', 'r')

    fl1 = file1.readlines()
    fl2 = file2.readlines()
    fl3 = []
    fl4 = []

    for i in fl1:
        text = i.replace('\n', '')
        fl3.append(text)

    for i in fl2:
        text = i.replace('\n', '')
        fl4.append(text)

    for i in range(len(fl1)):
        if fl3[i] != fl4[i]:
            print(f"Row-{i+1} in file1 is {fl3[i]} "
                  f"but row-{i+1} in file2 it is {fl4[i]}.")
except Exception as e:
    print(str(e))

