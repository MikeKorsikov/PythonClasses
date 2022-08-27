print('Exercise 5:')

given_symbol = input('Enter symbol: ')
count = 0

file = open('given_file.txt', 'r')
content = file.read()
file.close()

print('Original text:')
print(content)

# convert string to list of words
print('Text converted to list:')
con_lst = content.split()

print(con_lst)

# processing list
for i in con_lst:
    if i[0:1] == given_symbol:
        count += 1
    else:
        pass

# show result
print(f"\nNumber of words starting with [{given_symbol}] is {count}.")
