
class Sum:

    @staticmethod
    def sum( *args):

        sum=0
        for i in args:
            sum += i

        print(type(args))
        return sum


class main():

    print("sum of given number:",Sum.sum(1,2,3,4,5))


main()