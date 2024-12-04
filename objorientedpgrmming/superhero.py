class superhero:

    def __init__(self,name,suit):

        self.name=name
        self.suit=suit

    def __str__(self):
        return self.name
    
class spiderman(superhero):

    def __init__(self, name, suit):

        super().__init__(name,suit)
        

    def super_power(self):

        print("spider sense","web shooting")

spiderman_instance=spiderman("spiderman","spidersuit")
# spiderman_instance.super_power()

# print(spiderman_instance)

class minnalmurali(superhero):

    def __init__(self, name, suit):
        super().__init__(name,suit)

    def super_power(self):

        print("running","jumping")

minnalmurali_instance=minnalmurali("minnalmurali","minnalsuit")
print(minnalmurali_instance)

minnalmurali_instance.super_power()
