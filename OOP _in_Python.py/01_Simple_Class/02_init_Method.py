class Animal():
    def __init__(self,name,spice):
        self.name = name 
        self.spice = spice 
    
    def show(self):
        print("Animal is " + self.name + " Spice is " + self.spice)

a= Animal("Dog", "Mammal")
a1 = Animal("Cat", "Pet")

a.show()
a1.show()