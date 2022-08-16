#example 1 (AND)
print("\nExample 1: ")
hours = int(input("Enter hours: "))
if hours >= 12 and hours <24:
    print("PM")
elif hours >= 0 and hours < 12:
    print("AM")
else:
    print("Error")

#example 2 (OR)
print("\nExample 2: ")
mark = int(input("Enter mark: "))
if mark == 12 or mark == 11:
    print("Perfect!")
else:
    print("Ok")

#example 3 (NOT)
print("\nExample 3: ")
passed = True

if not passed:
    print("Bad")
else:
    print("Good")


#example 4 (IN)
print("\nExample 4: ")
message = "Hello World!"
text = "Hello"

print(text in message)
if text in message:
    print(text + " is substring of " + message)
else:
    print("Not")

#example 5
print("\nExample 5: ")

language = "english"
curr_time = 12

if language == "english":
    if curr_time == 12:
        print("Ok")


# example 6 (cycles - WHILE)
print("\nExample 6: ")

num = 0

# while num < 5:
#     print(num)
#     num += 1

while True:
    num += 1

    if num == 5:  # to exclude 5 from the list
        continue
    if num >= 10:
        break

    print(num)


# example 7 (cycles)
print("\nExample 7: ")

number_of_entries = 0
sum_of_digits = 0

while True:
    digit = int(input("enter number: "))
    if digit > 0 or digit < 0:
        number_of_entries += 1
        sum_of_digits += digit
    if digit == 0:
        average = sum_of_digits / number_of_entries
        print("Average result is: ", average)
        break

# example 8 (cycles)
# 2. Пользователь вводит числа с клавиатуры
# если ввел 0 -> вывести на экран максимальное и минимальное числа
print("\nExample 8: ")
smallest = 0
largest = 0

while True:
    digit = int(input("enter number: "))

#Solution From Vlad
Result = 0
size = 0
while True:
  num = int(input("Введите число: "))
  result+=num
  size+1
  if num == 0:
    break
resultAll = result / size
print("Среднее арифметическо: ",resultAll)
minNum = 100;
maxNum = 1;
while True:
  num = int(input("Введите число: "))
  if minNum > num:
    minNum=num
  if maxNum < num:
    maxNum=num
  if num == 0:
    break
print("Максимальное число: ",maxNum)
print("Минимальное число: ",minNum)
