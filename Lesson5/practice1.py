#PZm3p1

# Example 1
print("\nExample 1:")
text = input("Please enter your full name: ")
print("In reverse:", text[::-1])

# Example 2
print("\nExample 2:")
text2 = input("Please enter combination of characters: ")
total_length = len(text2)
print(f"\tTotal number of characters in a string: {total_length}")
total_digits = 0
total_char = 0
total_other = 0

for i in text2:
    if i.isdigit():
        total_digits += 1
    elif i.isalpha():
        total_char += 1
    else:
        total_other += 1
print(f"\tNumber of characters in a string - {total_char}, "
      f"digits - {total_digits} and other characters - {total_other}.")

# Example 3
print("\nExample 3:")
input_text = input("Please enter combination of characters: ")
unique_char = input("Please enter symbol to be found: ")
counter = 0

for i in input_text.lower():
    if i == unique_char.lower():
        counter += 1
print(f"\tSymbol '{unique_char}' was mentioned {counter} times in a string.")

# Example 4
print("\nExample 4:")
input_text = input("Please enter a sentence: ").lower()
unique_word = input("Please enter a word to be found: ")
frequency = 0

input_text_norm = input_text.split()
# print(input_text_norm)
for i in input_text_norm:
    if i == unique_word.lower():
        frequency += 1

print(f"\tWord '{unique_word}' is mentioned {frequency} times.")

# Example 5
print("\nExample 5:")
input_text = input("Please enter a sentence: ").lower()
original_word = input("Please enter a word to be replaced: ").lower()
replacement = input("Please enter replacement word: ").lower()

pur_orig = original_word.strip()
pur_repl = replacement.strip()

updated_text = input_text.replace(pur_orig, pur_repl)
print(updated_text.capitalize())
