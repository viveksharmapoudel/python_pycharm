
def func(name : str, age : int , weight: float) -> str:         ##function annotation doesn't has any used in execution just used for documentation
    print(name)
    print(age)
    print(weight)

    return "{} is {} yrs old and weighs {} kg".format(name,age,weight)


print(func("vivek",24,70))
print(func(4556,"fjkfsdj","fekfj"))
