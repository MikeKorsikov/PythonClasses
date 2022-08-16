# OPEN, PROCESS, CLOSE files

# A - create .txt file
todos = open('todos.txt', 'a')
# r - reading
# w - writing
# a - appending
# x - new file

# B - process (edit) file with print()

print('Put out the trash', file=todos)
print('Feed the cat', file=todos)
print('Prepare tax return', file=todos)

# C - close file with .close()
todos.close()

# Reading data with .open()

tasks = open('todos.txt')

# iterating through lines in file
for chore in tasks:
    print(chore, end='')
tasks.close()

# alternative way of processing file

with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')