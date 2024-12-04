class shipping:

    def calculate_shipping_cost(self,weight):

        print(weight*5)

class xpresshipping(shipping):

     def calculate_shipping_cost(self,weight):

        print(weight*20)


class standrdshipping(shipping):

     def calculate_shipping_cost(self,weight):

        print(weight*10)


xpresshipping_instance=xpresshipping()
xpresshipping_instance.calculate_shipping_cost(10)

std_instance=standrdshipping()
std_instance.calculate_shipping_cost(10)



#class
#object
#__init__
#super()
#self
#inheritence
    #single
    #multilevel
    #multiple
#polymorphism
    #mthd overloading
    #mthd overriding
#abstraction
    #hiding implementation details