#
import re

temp = []

with open('text.txt', 'r') as f:
    temp = list(filter(lambda x: len(x) > 7, f.read().split()))

print(temp)

with open('newfile.txt', 'w') as f:
    f.write(''.join(temp))
