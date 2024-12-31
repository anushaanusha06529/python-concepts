class Bank:
    bank_name='sbi'
    bank_ifsc=1234
    bank_branch='kizikistan'
    bank_roi=7
    def __init__(self,n,a,b):
        self.cname=n
        self.cage=a
        self.cbal=b

    @classmethod
    def modify_roi(cls):
        print('cls value is',cls)
        new=int(input('enter a value'))
        cls.bank_roi=new
        print('roi is changed')

Anu=Bank('Anu',23,98447)
Megha=Bank('Megha',23,86877)
print('Anu',Anu)
print(Bank.bank_roi)
print(Anu.bank_roi)
Bank.bank_roi
