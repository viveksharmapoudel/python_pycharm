class Time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second


    def __str__(self):
        return "{}::{}::{}".format(self.hour,self.minute,self.second)

    def __add__(self, otherTime):
        resultTime =Time()
        resultTime.second=otherTime.second +self.second

        temp_second_carry=0
        if( resultTime.second>60):
            temp_second_carry+=1
            resultTime.second=resultTime.second%60


        resultTime.minute=otherTime.minute+self.minute+ temp_second_carry
        temp_minute_carry=0
        if(resultTime.minute>60):
            temp_minute_carry+=1
            resultTime.minute=resultTime.minute%60

        resultTime.hour=otherTime.hour+self.hour+temp_minute_carry

        return resultTime





def main():
    t1 =Time(15,20,40)

    print(t1.__str__())
    t2= Time(30,40,50)
    print(t1+t2)

main()