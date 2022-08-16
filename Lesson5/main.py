# Strings

# Example 1
message = "Hello world \
I am \
here"
print(message)

# Example 2
text = ("zzzzzz"
"xxxxx")

print(text)

# Example 3
text1 = '''
text text text
'''

print(text1)

# Example 4
path = r"C:\Users\user\Desktop\Apps"
print(path)

# Example 5
cats = 10
dogs = 20

print(f"Cats {cats} and dogs {dogs}")

# Example 6
cat = "kitty"
dog = "doggy"
result2 = "Cat is {0} and dog is {1}".format(cat, dog)
print(result2)

# Example 7
text2 = "Hello world"
item = text2[0]
print(item)

item = text2[1]
print(item)

# Example 8
# N.B. string is immutable and can't be edited, only replaced
text = "Hello world"
print(len(text))
print(text[len(text) - 1])

# Example 9
text = "Hello world"
for i in range(len(text)):
    print(text[i], end=" ")
print("\n")
for symbol in text:
    print(symbol, end=" ")

# Example 10
text = "Hello world"
print(text[:])
print(text[0:])
print(text[0:5])
print(text[0:11:2])
print(text[::-1])

# Example 11 (concatenation)
one = "Love "
two = "you"

print(one + two)

# Example 12
print("qs" * 5)
print("a" > "b")

# Example 13
text = "Mykola"
print(text.upper())

text = "mykolA"
print(text.lower())

# Example 14 (Unicode order)
print(ord("a"))
print(ord("b"))

# Example 15 https://docs.python.org/3/library/stdtypes.html
text = "Hello world"
if 'hello' in text.lower():
    print("Ok")
else:
    print("Not ok")

# Example 16 (calling functions without perimeters)
text = "hELo WOrlD"
print(text.capitalize())
print(text.title())
print(text.isalpha())
print(text.islower())
print(text.isdigit())
print(text.isnumeric())

# Example 17 (calling functions with perimeters)
file_name = "python.py"
start = file_name.startswith("python")
end = file_name.endswith("py")
print(start)
print(end)

# Example 18
test = "adsfgsf "
print(test.strip())

# Example 19 (looking for index)
text = "text test text"
print(text.find("tes")) #left to right
print(text.rfind("tex")) #right to left

# Example 20 (replace)
old_phone = "+48-513-523-937"
updated_phone = old_phone.replace("-", " ")
print(updated_phone)

new_phone = old_phone.replace("-", "_", 1)
print(new_phone)

# Example 21
test = "he following, sections describe, \
the standard types, that are built, into the interpreter."

sp1 = test.split()
print(sp1)

sp2 = test.split(", ")
print(sp2)

sp3 = test.split(" ", 3)
print(sp3)

# Example 22
words = ['he', 'following,', 'sections', 'describe,', 'the', 'standard',
         'types,', 'that', 'are', 'built,', 'into', 'the', 'interpreter.']
sentence = " ".join(words)
print(sentence)
