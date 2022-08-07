print("\nExercise 1:")

try:
    # access data
    file = open('given_file.txt', 'r')
    content = file.read()
    file.close()

    # process data
    content_lstd = content.split()
    content_cond = []

    for i in content_lstd:
        if len(i) >= 7:
            content_cond.append(i)
    content_jnd = " ".join(content_cond)

    # copy processed data
    file2 = open('processed_data.txt', 'w')
    file2.write(content_jnd)
    file2.close()

    print('Data was successfully processed and saved.')

except Exception as e:
    print(str(e))
