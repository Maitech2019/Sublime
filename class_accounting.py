# class Accounting

from class_employee import Employee

class Accounting(Employee):
	_departmentName = "accounting department"
	def __init__(self,name,salary):
		super().__init__(name,salary,self._departmentName)