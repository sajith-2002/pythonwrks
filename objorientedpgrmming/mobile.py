class mobile:

    def __init__(self,name,price,brand):

        self.name=name

        self.price=price

        self.brand=brand
        
    def display(self):

        print(self.name,self.price,self.brand)

mobile_instance1=mobile("1+",19000,"1+")

mobile_instance1.display()
