class Fibonacci:
    def __init__(self):
        self.first=0
        self.second=1

    def __iter__(self):
        return self
    def __next__(self):
        fibNum=self.first+self.second
        self.first=self.second
        self.second=fibNum
        return fibNum

fibseq =Fibonacci()
for i in range(10):
    print("fib:",next(fibseq))