class UsernameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self,*args,**kwargs)

try:
    userName=input("enter the username:")

    for char in  userName:
        if char.isdigit():
            raise UsernameError

except NameError:
    print("nameError occured")

except UsernameError:
    print("your user name cannot contain a number")

except:
    print("errorccureed")