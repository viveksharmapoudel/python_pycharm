import threading
import time
import random


class BankAccount(threading.Thread):

    accountBalance= 100
    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)

        self.name=name
        self.moneyRequest=moneyRequest

    def run(self):
        threadLock.acquire()

        BankAccount.getMoney(self)

        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdrawal ${} at {}".format(
            customer.name, customer.moneyRequest,
            time.strftime("%H:%M:%S",time.gmtime())
        ))

        if BankAccount.accountBalance-customer.moneyRequest>0:
            BankAccount.accountBalance-= customer.moneyRequest
            print("new account balance : ${}".format(
                BankAccount.accountBalance
            ))
        else:
            print("not enough money in account")
            print("Current balance : ${}".format(
                BankAccount.accountBalance))
        time.sleep(3)

# Create a lock to be used by threads
threadLock = threading.Lock()

vivek=BankAccount("Vivek",10)
prabesh=BankAccount("prabesh",100)
shiva=BankAccount("Shiva",50)

vivek.start()
prabesh.start()
shiva.start()

vivek.join()
prabesh.join()
shiva.join()

print("Execution Ends")
