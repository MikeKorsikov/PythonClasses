# sorting data (part 1)

list = [4, -2, 1, -5, 8]

list2 = ['Bob', 'Anna', 'Joe', 'Nick']

list.sort()
print(list)

list.sort(reverse=True)
print(list)


# Bubble Sort

numbers = [5,2,4,7,6]

def myBubbleSort(myList):
    for i in range(len(myList)-1):
        for j in range(len(myList)-i-1):
            if myList[j]<myList[j+1]:
                temp=myList[j]
                myList[j]=myList[j+1]
                myList[j+1]=temp

def printList(myList):
    for index, elem in enumerate(myList):
        print("element {}: {}".format(index+1, elem))

print("Original list:")
printList(numbers)
myBubbleSort(numbers)
print("Sorted list:")
printList(numbers)