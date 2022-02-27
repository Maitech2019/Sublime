#run program

from class_accounting import Accounting
from class_sales import Sales
from class_programmer import Programmer


account = Accounting("May", 20000)   

print(account.__str__())
print("annual income: " +str(account._getIncome()))

print(account._showData())        #use _showData() from super()

programmer = Programmer("Jo",4000,3,"Gaming")
programmer._showData()            #use over riding method _showdata() from suClass Programmer

sale = Sales("Drew", 30000, "Chaiangmai")
sale._showData()
print(sale.__str__())             #use over rinding method __str__ in subClass Sales
print("annual income: " +str(sale._getIncome(300,1)))           #use overloading method(set default parameter =0, can use it or not)
