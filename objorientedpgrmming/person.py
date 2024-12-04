class Person:

    def __init__(self,name,age):

        self.name=name
        self.age=age
    def disp_person_info(self):

        print(self.name,self.age)


class Employee:

    def __init__(self,eid,salary):

        self.eid=eid
        self.salary=salary
    def disp_employee_info(self):

        print(self.salary,self.eid)


class Manager(Person,Employee):


    def __init__(self, age,name,eid,salary,department):

        Person.__init__(age,name)

        Employee.__init__(eid,salary)

        self.department=department

    def disp_manager_info(self):

        self.disp_person_info()
        self.disp_employee_info()

        print(self.department)



manager_instance=Manager(32,"hari","fkfm",54000,"hr")
manager_instance.display(manager_instance)
        

    