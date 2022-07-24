print('\nExercise 6 Replace word in a text:\n')

try:
    text = open('text.txt', 'r')
    text = text.read() #convert to string
    ls_text = text.split() # converted to list
    # print(ls_text)

    print('Here is a given text to work with:\n')
    print(f'\t"\033[1;3m{text}...\033[0m"')

    old_w = input('\t\nWhat word are you looking for? ')
    x = text.count(old_w) #count number of times word is mentioned
    n = len(ls_text)

    if x > 0:
        print(f'Word [{old_w.upper()}] is found [{x}] time(s).')
        new_w = input(f'What word do you want to replace [{old_w.upper()}] with? ')

        for i in range(n):
            word_norm_dot = ls_text[i].replace('.', '')
            word_norm_que = word_norm_dot.replace('?', '')
            word_norm_com = word_norm_que.replace(',', '')

            if word_norm_com.lower() == old_w.lower():
                ls_text[i] = new_w.upper()

        joined_list = " ".join(ls_text)

        print('Here is a text with replaced words:\n')
        print(f'\t"\033[1;3m{joined_list}...\033[0m"')


    else:
        print(f'Word [{old_w.upper()}] is not found')

except Exception as e:
    print(str(e))