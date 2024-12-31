class Gopalappa:
    house='1bhk'
    bike='chetak'
    money=100000
gangamma=Gopalappa()

class Seenu(Gopalappa):
    bik='ktm'
    car='kia'

Anu=Seenu()

#Accessing the parent class properties by using parentclass(PC),parent classobj(PCO),childclass(CC),childclassobj(CCO)
print(Gopalappa.money)
print(gangamma.money)
print(Seenu.money)
print(Anu.money)

#modify the parent class property by using parent class 
Gopalappa.money=50000
print(Gopalappa.money)
print(gangamma.money)
print(Seenu.money)
print(Anu.money)

#it modify in PC,PCO,CC and as wll modify parent class properties by using parent class object
gangamma.money=40000
print(Gopalappa.money)
print(gangamma.money)
print(Seenu.money)
print(Anu.money)

#it modify in PCO modifying pqrent class properties by using child class
Seenu.money=3000
print(Gopalappa.money)
print(gangamma.money)
print(Seenu.money)
print(Anu.money)

#it modify in CC and as well as CCO modifying parent class properties by using child class object
Anu.money=5000
print(Gopalappa.money)
print(gangamma.money)
print(Seenu.money)
print(Anu.money)
