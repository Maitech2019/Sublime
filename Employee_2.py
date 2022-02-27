#Employee_2

class Employee:
	#class variable
	_minSalary = 12000
	maxSalary = 40000
	companyName = "Consoto Company"

	def __init__(self,name,salary,department):
		#instance variable
		self._name = name
		self._salary = salary
		self.department = department

	def _showData(self):
		print("employee name: "+ self._name)
		print("employee salary: ",format(self._salary))
		print("employee department: "+ self.department)

	def _getIncome(self):
		return self._salary *12

	def __str__(self):
		return("employee name: {}, department name: {}, salary: {}".format(self._name,self.department,self._salary))

class Accounting(Employee):
	_departmentName = "accounting department"
	def __init__(self,name,salary):
		super().__init__(name,salary,self._departmentName)
	

class Sales(Employee):
	_departmentName = "sales department"
	def __init__(self,name,salary,area):
		super().__init__(name,salary,self._departmentName)
		self.area = area

	def _showData(self):
		print("employee area sales: "+self.area)

class Programmer(Employee):
	_departmentName = "programmer department"
	def __init__(self,name,salary,experience,skill):
		super().__init__(name,salary,self._departmentName)
		self.exp = experience
		self.skill = skill

	def _showData(self):
		super()._showData()
		print("employeer experience: " +str(self.exp))
		print("employee skill: "+self.skill)



account = Accounting("May", 20000)   
print(account.__str__())

print(account._getIncome())
print(account._showData())        #use _showData() from super()

programmer = Programmer("Jo",4000,3,"Gaming")
programmer._showData()            #use over riding method _showdata() from suClass Programmer

sale = Sales("Drew", 30000, "Chaiangmai")
sale._showData()