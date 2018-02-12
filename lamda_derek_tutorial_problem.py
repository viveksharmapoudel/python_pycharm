
def isNumOdd(num):
    if num%2==0:
        return False
    else:
        return True

def surrFunc(isNumOdd, lst):

    result=[]
    for i in lst:
        if isNumOdd(i):
            result += [i]
    return result


def main():
    print(surrFunc(isNumOdd,[1,2,3,4,5]))


main()
