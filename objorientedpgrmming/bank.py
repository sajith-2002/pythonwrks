class bank:

    def __init__(self,accno,balance,ac_type,cust_name):

        self.accno=accno
        self.balance=balance
        self.ac_type=ac_type
        self.cust_name=cust_name





    def deposit(self,amount):

        self.balance+=amount

        print(f"ur acc{self.acno} has been credited with amount{amount} avl bal{self.balance}")


    def withdraw(self,amount):

        if self.balance>=amount:

            self.balance-=amount

            print(self.balance)

        else:


            print("insuff bal")
            

    def get_bal(self):

        print(self.balance)


customer_instance1=bank(10000,2500,"savings","b;abla")

customer_instance1.withdraw(500)



    