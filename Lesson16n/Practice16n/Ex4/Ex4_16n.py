# copying from one file to another file
path1 = "/Users/mykolakorsikov/PycharmProjects/Python/Lesson16n/Ex4/example.txt"
path2 = "/Users/mykolakorsikov/PycharmProjects/Python/Lesson16n/Ex4/result.txt"

with open(path1, "r") as sourceFile, open(path2, "w") as destinationFile:
    # read the content from example.txt
    fileContent = sourceFile.read()
    # write the content to result.txt
    destinationFile.write(fileContent)
