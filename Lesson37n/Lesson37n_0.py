# Multithreading in Python
# https://www.geeksforgeeks.org/multithreading-python-set-1/

import os
import time
#
# while True:
#     print(os.getpid())
#     time.sleep(3)


import threading

def foo(a, b):
    time.sleep(3)
    print('Sum', a+b)

t1 = threading.Thread(target=foo, args=(3, 2), daemon=True)
t1.start()
t1.join(0.125)
if t1.is_alive():
    print('Thread is alive')
else:
    print('The end')
print('Main')