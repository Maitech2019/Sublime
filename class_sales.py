#class Sales

from class_employee import Employee

class Sales(Employee):
	_departmentName = "sales department"
	def __init__(self,name,salary,area):
		super().__init__(name,salary,self._departmentName)
		self._area = area

	def _showData(self):
		print("employee area sales: "+self._area)
		print("#############")

	def __str__(self):
		return(super().__str__()+", employee area sales: {}".format(self._area))