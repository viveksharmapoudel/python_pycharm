class Dog:

    no_of_dogs=0

    def __init__(self, name="unknown"):
        self.name= name
        Dog.no_of_dogs+=1


    @staticmethod
    def getNoOfDogs():
        print("there are {} of dogs available".format(Dog.no_of_dogs))



def main():

    rocky= Dog("Rocky")

    Bitto= Dog("Bitto")




    Dog.getNoOfDogs()


main()

