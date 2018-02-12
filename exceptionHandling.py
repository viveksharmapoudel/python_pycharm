try:
    alist = [1, 2, 3]
    print(alist[3])

except IndexError:
    print("there is some index error")          ##especially dedicated to index error

except:

    print("unknown error occured")              ##generalized exception for the error


finally:
    print("code is completed")







