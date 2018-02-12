class Dog:
    def __init__(self, name="", height=0,weight=0):
        self.name=name
        self.height=height
        self.weight=weight

    def dog_name(self):
        print("name of the dog is:",self.name)
    



def main():
    adog= Dog("Rocky",20,40)
    adog.dog_name()



main()

