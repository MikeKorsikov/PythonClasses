#

import threading

event = threading.Event()


def function1():
    print('Function1')
    event.set()


th = threading.Thread(target=function1).start()

event.wait()
event.clear()

