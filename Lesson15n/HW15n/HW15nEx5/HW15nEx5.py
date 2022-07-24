print('\nExercise 5 Finding given word:\n')

try:
    print('What word are you looking for?')
    word = input('>>> ')

    text = open('text.txt', 'r')
    text = text.read()

    x = text.count(word)
    print(f"Word [{word}] is mentioned {x} times in the text.")

except Exception as e:
    print(str(e))