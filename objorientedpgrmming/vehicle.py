class car:

    def __init__(self,name,brand,fuel):

        self.name=name
        self.brand=brand
        self.fuel=fuel


    def display(self):

        print(self.name,self.brand,self.fuel)

    def __str__(self):
        
        return self.brand

car_instance1=car("swift","suzu","petrol")

car_instance1.display()

print(car_instance1)
        