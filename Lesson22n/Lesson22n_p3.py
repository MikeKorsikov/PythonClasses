# Lesson 9 book


def checkStudentSuccess(name, score):
    if score >= 90:
        print("{} has excellent level".format(name))
    elif 75 <= score < 90:
        print("{} has good level".format(name))
    elif 60 <= score < 75:
        print("{} has average level".format(name))
    else:
        print("{} has poor level".format(name))


def checkPupilSuccess(name, score):
    if score >= 10:
        print("{} has excellent level".format(name))
    elif 7 <= score < 10:
        print("{} has good level".format(name))
    elif 4 <= score < 7:
        print("{} has average level".format(name))
    else:
        print("{} has poor level".format(name))


# checkStudentSuccess("Jane", 78)
# checkPupilSuccess("Bob", 6)

#
userLogs = ['Admin123', 'superUSER', 'GOODstudent']
userBYears = [2000, 2010, 2005]


def listMaker1(myList):
    result = []
    for item in myList:
        result.append(item.lower())
    return result


def listMaker2(myList):
    result = []
    for item in myList:
        result.append(2022 - item)
    return result


# newList1 = listMaker1(userLogs)
# newList2 = listMaker2(userBYears)
# print(newList1)
# print(newList2)

#

