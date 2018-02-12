num1,num2=input("two numbers to be divided").split()

try:
    quotient=int(num1)/int(num2)
    print("{}/{}={}",num1,num2,quotient)

except ZeroDivisionError:
    print("you try to divided by zero")

else:
    print("no exception raised")

finally:
    print("end of the code")
