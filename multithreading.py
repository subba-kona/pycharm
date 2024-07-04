import threading
from threading import *

print(current_thread().name)

def func1() :
    print("in child function")
    print(current_thread().name)

def func2() :
    print("in child function 2")
    print(current_thread().name)

childThread = Thread(target=func2)
childThread.start()

childThread = Thread(target=func1)
childThread.start()


print(current_thread().name)