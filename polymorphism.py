class Bank_v1():
    bank_name='sbi'
    bank_ifsc=1234
    bank_branch='bangalore'
    def __init__(self,cn,ca,cb,cac):
        self.cname=cn
        self.cage=ca
        self.cbalance=cb
        self.caccount=cac


    @classmethod
    def display_bank_details(cls):
        print(f'name of the bank {cls.bank_name}')
        print(f'ifsc of the bank {cls.bank_ifsc}')
        print(f'branch of the bank {cls.bank_branch}')


    def customer_details(self):
        print(f'name off the customer {self.cname}')
        print(f'age off the customer {self.cage}')
        print(f'balance off the customer {self.cbalance}')
        print(f'account off the customer {self.cname}')



    @staticmethod
    def get_int_value():
        amt=int(input('enter value'))
        return amt


    def withdraw(self):
        amt=self.get_int_value()
        if amt>=self.cbalance:
            print('sry ur bal is low')
        else:
            self.cbalance=amt
            print('withdraw sucessfully',self.cbalance)

    def deposite(self):
        amt=self.get_int_value()
        self.cbalance+=amt
        print('money deposite sucessfully')

class Bank_v2(Bank_v1):
    bank_branch='pavagada'
    bank_roi=7
    def __init__(self,cn,ca,cb,cac,cp):
       Bank_v1.__init__(self,cn,ca,cb,cac)
       self.cpin=cp

       
    @classmethod
    def display_bank_details(cls):
       super().display_bank_details()
       print(f'roi of bank {cls.bank_roi}')

        
    def withdraw(self):
        epin=selg.get_int_value()
        if epin==self.cpin:
            Bank_v1.withdraw(self)
        else:
            print('incorrect pin')
        

    @staticmethod
    def get_str_value():
        sv=input('enter str value')
        return sv

    @classmethod
    def change_branch(cls):
        nb=cls.get_str_value()
        cls.bank_branch=nb
        print('branch is changer')


    @classmethod
    def change_roi(cls):
        nr=cls.get_int_value()
        cls.bank_roi=nr
        print('roi changed sucessfully')


Anu=Bank_v2('anu',22,1878,1779,3456)
Anu.display_bank_details()
        
            
        
