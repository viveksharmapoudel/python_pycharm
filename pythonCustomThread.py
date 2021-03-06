import threading
import time
import random


class CustThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name=name



    def run(self):
        getTime(self.name)
        print("Threat",self.name,"Execution Ends")

def getTime(name):
    print("Thread {} sleeps a {}".format(name, time.strftime(
            "%H:%M:%S", time.gmtime())))
    randSleepTime = random.randint(1, 5)

    time.sleep(randSleepTime)


thread1= CustThread("1")
thread2=CustThread("2")

thread1.start()
thread2.start()

print("Thread is alive:",thread1.is_alive())
print("Thread is alive:",thread2.is_alive())

print("Thread 1 Name:",thread1.getName())
print("Thread 2 Name:",thread2.getName())

thread1.join()
thread2.join()

print("execution Ends:")