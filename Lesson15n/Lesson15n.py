# files

try:
    file = open('Practice15n/test.txt', 'a')
    try:
        file.write('\nhello again?')
    except Exception as e:
        print(e)
    finally:
        file.close()
except Exception as e:
    print(e)


# reading content
try:
    with open('Practice15n/test.txt', 'r') as f:
        line = f.readline()
        while line:
            print(line)
            line = f.readline()
except Exception as e:
    print(f"Open file error: {str(e)}")

# iterate file content
try:
    with open('Practice15n/test.txt', 'r') as f:
        line = f.readlines()
        for i in line:
            print(i)
except Exception as e:
    print(f"Open file error: {str(e)}")

# to print first line
try:
    with open('Practice15n/test.txt', 'r') as f:
        line = f.readlines()
        print(line[0])
except Exception as e:
    print(f"Open file error: {str(e)}")

# to check if readable
try:
    with open('Practice15n/test.txt', 'r') as f:
        if f.readable():
            line = f.readlines()
            for i in line:
                print(i)
except Exception as e:
    print(f"Open file error: {str(e)}")