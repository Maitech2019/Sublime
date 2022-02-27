#class Programmer

from class_employee import Employee


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