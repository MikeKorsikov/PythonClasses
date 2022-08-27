print('\nExercise 6 Replace word in a text:\n')

try:
    text = open('given_file2.txt', 'r')
    text = text.read()  # convert to string
    text = text.split('\n')  # breakdown each raw to be separate item to be added to list
    new_text = []

    print('Here is a given text to work with:')
    print(f'\033[1;3m{text}\033[0m')

    symbol_to_replace = '*'
    new_symbol = '&'

    for word in text:
        new_word = ''
        for symbol in word:
            if symbol == symbol_to_replace:
                symbol = symbol.replace(symbol_to_replace, new_symbol)
                new_word += symbol
            elif symbol == new_symbol:
                symbol = symbol.replace(new_symbol, symbol_to_replace)
                new_word += symbol
            else:
                new_word += symbol
        new_text.append(f"{new_word}\n")

    print('\nProcessed text:')
    print(new_text)

    joined_text = " ".join(new_text)
    print(joined_text)

    # recording result to destination file
    dest_file = open('destination_file.txt', 'w')
    dest_file.write(joined_text)
    dest_file.close()

except Exception as e:
    print(str(e))
