# Multithreading in Python (part 2)
# https://webdevblog.ru/vvedenie-v-potoki-v-python/

import os
import threading
import time
from threading import *

# print(os.cpu_count())


class Th(threading.Thread):
    def __init__(self, var):
        Thread.__init__(self)
        self.daemon = True
        self.var = var

    def run(self):
        num = 1
        while True:
            x = 0.5/(num*2)
            num += 1
            print(f"num = {num}, x = {x}")
            time.sleep(self.var)


th = Th(1)
th.start()
time.sleep(2)