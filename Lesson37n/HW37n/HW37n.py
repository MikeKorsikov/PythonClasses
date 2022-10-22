# HW on multithreading
# Process - instance of computer program
# Thread (Поток)- entity within a process (subset of process)

import os
import random
import threading

list_of_numbers = []
sum_of_digits = 0
count = 0


def function1(lock):
    global list_of_numbers
    global count

    print(f"\n(1) "
          f"Process ID: {os.getpid()}, "
          f"thread name: {threading.current_thread().name}, initiated...")

    lock.acquire()
    for i in range(random.randint(1, 10)):
        x = random.randint(0, 10)
        count += 1
        list_of_numbers.append(x)
    print(f"(1) List of generated digits is: {list_of_numbers}.")
    lock.release()


def function2():
    print(f"\n(2) "
          f"Process ID: {os.getpid()}, "
          f"thread name: {threading.current_thread().name}, initiated...")
    global sum_of_digits
    for i in list_of_numbers:
        sum_of_digits += i
    print(f"(2) Sum of {count} digits in the list is: {sum_of_digits}.")


def function3():
    print(f"\n(3) "
          f"Process ID: {os.getpid()}, "
          f"thread name: {threading.current_thread().name}, initiated...")
    alt_count = len(list_of_numbers)
    alt_sum = sum(list_of_numbers)
    av_value = alt_sum / alt_count
    print(f"(3) Average (rounded) value is: {int(av_value)}.")


def main():
    # creating thread
    lock = threading.Lock()
    t1 = threading.Thread(target=function1, args=(lock,), name='t1')
    t2 = threading.Thread(target=function2, name='t2')
    t3 = threading.Thread(target=function3, name='t3')

    #
    print(f"*** Main thread is: {threading.main_thread().name} ***")

    # starting 1-st thread
    t1.start()
    # Wait until the 1-st thread terminates
    t1.join()

    # start 2-nd and 3-rd thread
    t2.start()
    t3.start()

    # Wait until the 2-nd and 3-rd threads terminate
    t2.join()
    t3.join()

    print("\nSession terminated!")


if __name__ == "__main__":
    main()
