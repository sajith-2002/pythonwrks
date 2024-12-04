class Grandparent:

    def m1(self):

        print("grandparent class m1 mthd")

class parent:

    def m2(Self):

        print("parent class m2 mthd")

class child (parent,Grandparent):

    def m3(self):

        print("child class m3 mthd")

child_instance=child()
child_instance.m3()
child_instance.m2()
child_instance.m1()


###############################################################3



class Grandparent:

    def m(self):

        print("grandparent class m1 mthd")

class parent:

    def m(Self):

        print("parent class m2 mthd")

class child (Grandparent,parent):

    def m3(self):

        print("child class m3 mthd")

child_instance=child()
child_instance.m3()
child_instance.m()