#mthd overloading (samr name diff no of parameter)

# but in python no mthd overloading u can use *args

class operations:

    def add(self,num1,num2):

        print(num1+num2)


    def add(self,num1,num2,num3):

        print(num1+num2+num3)



obj=operations()
obj.add(10,20,30)

    