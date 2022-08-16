# PZm3p2

# Example 1
print("\nExample 1:")
original_text = input("Please enter a sentence: ")
br_text = original_text.split(".")
up_text = []

for i in br_text:
    a = i.lstrip()
    b = a.rstrip()
    c = b.capitalize()
    up_text.append(c)
    print(c)
print(up_text)
sentence = ". ".join(up_text)
print(sentence)

# Example 2
print("\nExample 2:")