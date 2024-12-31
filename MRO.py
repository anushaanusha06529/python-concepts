class A:
    abc=100
    def __init__(self,a):
        self.a=a
        print('__init__')
oa=A(23)
print(oa.__dict__)
print(A.__dict__)


#MRO is used to specify the order in which we have to execute the method in case of inheritance

