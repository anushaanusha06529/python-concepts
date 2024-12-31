class Bank:
    bank_name='sbi'
    bank_ifsc=1234
    bank_branch='kizikistan'
    def __init__(self,cn,cac,cb):
        self.cname=cn
        self.caccount=cac
        self.cbalance=cb

    def customer_details(self):
        print(f'name of the customer {self.cname}')
        print(f'account of the customer {self.caccount}')
        print(f'balance of customer {self.cbalance}')

    def withdraw(self):
        amt=int(input('enter amount'))
        if self.cbalance>=amt:
            self.cbalance-=amt
            print('amt withdraw sucessfully')
        else:
            print('insufficient balance')

    def deposite(self):
        amt=int(input('enter amount'))
        if amt>0:
            self.cbalance+=amt
            print('deposite sucessful')
        else:
            print('pls enter more than 1')





Anu=Bank('anu',879743094720,100000)
seenu=Bank('seenu',834684298,30000)

Anu.deposite()
Anu.customer_details()
