class bankaccount:

    def __init__(self,cust_name,mpin,acc_type,balance):

        self.cust_name=cust_name
        self.__mpin=mpin
        self.acc_type=acc_type
        self.__balance=balance

    def get_balance(self):

        print(self.__balance)

    def __str__(self):

        return self.cust_name
    
bankaccount_instance=bankaccount("hari",2345,"savings",45000)

print(bankaccount_instance)
        