print("\nExercise 2 copy rows in the same order:")

try:
    # access data
    with open('given_file.txt', 'r') as file:
        content = file.readlines()
    file.close()

    # record data
    with open('processed_data.txt', 'a') as file2:
        for row in content:
            file2.write(row)
    file2.close()

    print('Data was successfully processed and saved.')

except Exception as e:
    print(str(e))
