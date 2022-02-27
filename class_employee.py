#class Employee

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

	def _getIncome(self,bonus=0,overtime=0):
		return (self._salary *12)+bonus+overtime

	def __str__(self):
		return("employee name: {}, department name: {}, salary: {}".format(self._name,self.department,self._salary))