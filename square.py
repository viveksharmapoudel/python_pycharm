class Rectangle:
    def __init__(self ,height="0",width="0"):
        self.height=height
        self.width=width


    ##getter and setters

    @property
    def height(self):
        return self.__height


    @height.setter
    def height(self ,value):
        if value.isdigit():
            self.__height= value


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value

    def getArea(self):
        return (int(self.__height)*int(self.__width))


def main():
    arect= Rectangle()
    height = input("enter the height of the rectangle")
    width =input("enter the width of the rectangle")

    arect.height=height
    arect.width=width
    print("height entered is", arect.height)
    print("widht entered is",arect.width)
    print("the area is",arect.getArea())

main()



