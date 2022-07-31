# files (part 2)

# (1) open(fileName, mode)
FILE_NAME = open("/Lesson16n/Practice16n/Ex3/text.txt", 'r')

if FILE_NAME:
    print('File is open.')

# modes:
# r = read
# w = write
# a = append

# (2) read(size)
f = FILE_NAME
print(f.read(5))

# readline() to read single line

f = FILE_NAME
fl = f.readline()
print(fl)

sl = f.readline()
print(sl)

# readlines() to read all lines (content is presented as list [])

f = FILE_NAME
al = f.readlines()
print(al)

# (3) write()
FILE_NAME = open("/Lesson16n/Practice16n/Ex3/text.txt", 'w')
FILE_NAME.write('sample text')

# writelines() to write several lines
FILE_NAME = open("/Lesson16n/Practice16n/Ex3/text.txt", 'w')
text_to_be_added = ['\nLine 1\n', 'Line 2']
FILE_NAME.writelines(text_to_be_added)

# (4) close()
try:
    global fl
    fl = open('/Lesson16n/Practice16n/Ex3/text.txt', 'r')
    fr = fl.read()
    print(fr)
finally:
    fl.close()
    if not fl.closed:
        print("File still open.")
    else:
        print("File is closed.")

# expression WITH
with open('test.txt', 'w') as f:
    f.write('Hello')


