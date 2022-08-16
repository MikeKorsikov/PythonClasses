# match using python3.10 (match not avaliable in earlier versions)
import time


# # match with tuples
# users = ('Tom', 'Bob', 'Daniel')
#
#
match users:
    case ('Tom', 'Bob', 'Daniel') | ('Alex', 'Nik'):
        print('Case 1')
    case ('Tom', 'Bob'):
        print('Case 2')
    case (_, _, _):
        print('Case3')
    case _:
        print('Case 4')

# measuring speed
# start_time = time.time()
#
# ls = [i for i in range(0, 10)]
# print(ls)
# print('--- %s seconds ---' % (time.time() - start_time))
#

# match with lists
# ls2 = ["Den", "Alex", "test"]
#
# match ls2:
#     case ["Alex", "Den"] | ["alex", "den"]:
#         print("Case 1")
#     case ["Den", "Alex", "Test"]:
#         print("Case 2")
#     case [f, s, th]:
#         print(f"{f}, {s}, {th}")

# match with dictionaries

ls3 = {1: "Flex", 2: "Den", 3: 'Marta', 4: "Sasha"}

match ls3:
    # case {1: "Alex", 2: "Den"} | {1: "alex", 2: "den"}:
    #     print("Case 1")
    # case {1: "Den", 2: "Alex", 3: "Test"}:
    #     print("Case 2")
    # case {1: f, 2: s, 3: th}:
    #     print(f"Case 3: {f}, {s}, {th}")
    # case {}:
    #     print("Case 4")
    case {1: v1, 2: v2, **keys}:
        for i in keys:
            print(i)
    case f:
        print(f"case 5 {f}")
