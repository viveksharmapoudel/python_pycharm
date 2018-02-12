class Animal:
    def __init__(self, birthType="unknown",bloodType="unknown",appearance="unknown"):
        self.__birthType = birthType
        self.__bloodType = bloodType
        self.__appearance = appearance

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self,value):
        self.__birthType=value


    @property
    def bloodType(self):
        return self.__bloodType

    @bloodType.setter
    def bloodType(self,value):
        self.__bloodType=value

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self,value):
        self.__appearance=value


    def __str__(self):
        return "It belongs to {} calss, {} is birthtype,{} is appearance, {} is bloodtype".format(type(self).__name__,self.birthType,self.appearance,self.bloodType)


class Mammal(Animal):
    def __init__(self,birthType="born alive",bloodType="warm blood",appearance="fur or hair",nursing="milk feed"):
        Animal.__init__(self,birthType,bloodType,appearance)

        self.__nursing=nursing


    @property
    def nursing(self):
        return self.__nursing


    @nursing.setter
    def nursing(self,value):
        self.__nursing=value


    def __str__(self):
      return super().__str__()+" and have nursing ability of {}".format(self.nursing)


class Reptile(Animal):
    def __index__(self,birthType="eggs",bloodType= "cold blood", appearance="dry scaled",walkingAbility="crawl"):
        Animal.__init__(self,birthType,bloodType,appearance)

        self.__walkingAbility=walkingAbility


    @property
    def walkingAbility(self):
        return self.__walkingAbility

    @walkingAbility.setter
    def walkingAbility(self,value):
        self.__walkingAbility= value


    def __str__(self):
        return  super().__str__(self)+"this walking ability is {}".format(self.walkingAbility)


def main():

    aAnimal = Mammal()

    print(aAnimal.__str__())



main()
