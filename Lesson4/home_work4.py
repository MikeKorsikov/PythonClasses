# MODULE 4 part1

# M4p1 - Exercise 1
print("M4p1 - Exercise 1")
palindrome = True
string_input = input("Enter word or phrase (to check if it is palindrome):")
trim_input = string_input.replace(' ', '')
norm_str = trim_input.lower()
for i in range(0, int(len(norm_str) / 2)):
    if norm_str[i] != norm_str[len(norm_str) - i - 1]:
        palindrome = False
if palindrome:
    print(f'{string_input} is a polindrome')
else:
    print(f'{string_input} is NOT a polindrome')

# M4p1 - Exercise 2
print("\nM4p1 - Exercise 2")
list_of_words = []
new_sent = []
ending = ""

text_input = input("Enter text (sentence):")
split_sent_into_words = text_input.split()

reserved_list = input("How many reserved words do you want to add to the list?")
for i in range(int(reserved_list)):
    if i == 0:
        ending = '-st'
    elif i == 1:
        ending = '-nd'
    elif i == 2:
        ending = '-rd'
    else:
        ending = '-th'
    word = input(f"Enter {i+1}{ending} reserved word:")
    word = word.lower()
    list_of_words.append(word)

for i in split_sent_into_words:
    i = i.lower()
    i = i.strip()
    i = i.replace('.', '')
    if i in list_of_words:
        i = i.capitalize()
    new_sent.append(i)

text_output = " ".join(new_sent)
print(f'{text_output}.')

# M4p1 - Exercise 3
print("\nM4p1 - Exercise 3")
text_input = input("Enter text (more than one sentence):")
sentence = 0

for i in text_input:
    if i == ".":
        sentence += 1

if sentence == 1:
    print(f"There is 1 sentence in the given text.")
else:
    print(f"There are {sentence} sentences in the given text.")