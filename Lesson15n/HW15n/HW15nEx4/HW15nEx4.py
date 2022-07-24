print('\nExercise 4 Finding longest row:\n')

try:
    textfile = open('textfile.txt', 'r')
    lf = textfile.readlines()
    lf_norm = []

    for i in lf:
        text = i.replace('\n', '')
        lf_norm.append(text)



    n = 0
    for i in lf_norm:
        row_len = len(i)
        if row_len > n:
            n = row_len

    print(f"List of given rows: {lf_norm}")
    print(f"Longest row has [{n}] symbols/digits.")

except Exception as e:
    print(str(e))