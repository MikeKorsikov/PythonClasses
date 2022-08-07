print("\nExercise 3 copy rows in reverse order:")

try:
    # access data
    with open('given_file.txt', 'r') as file:
        content = file.readlines()
    file.close()

    # process data
    content_proc = []
    content.reverse()
    for row in content:
        content_proc.append(row.strip())

    # record data
    with open('processed_data.txt', 'a') as file2:
        for row in content_proc:
            file2.write(f"{row}\n")
    file2.close()

    print('Data was successfully processed and saved.')

except Exception as e:
    print(str(e))