class Employee:
	num_of_emp = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.f_name = first
		self.l_name = last
		self.email = f"{first}{last}.@email.com"
		self.pay = pay
		Employee.num_of_emp += 1

	def fullname(self):
		return f"{self.f_name} {self.l_name}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang


class Manager(Employee):
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print("-->", emp.fullname())


class Department(Developer):
	def __init__(self, first, last, pay, prog_lang, dptm):
		super().__init__(first, last, pay, prog_lang)
		self.dptm = dptm

	def full_details(self):
		return f"{self.f_name} {self.l_name} - {self.dptm}"


dev_1 = Employee("Miles", "Bg", 5000)
dev_2 = Developer("Daniel", "philip", 6000, "Javascript")
dev_3 = Department('Mohammed', 'Essam', 70000, 'python', 'Junior dev')
mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_3)
mgr_1.print_emps()
mgr_1.remove_emp(dev_2)
print('---------------------')
mgr_1.print_emps()

# print(dev_2.email)
# print(dev_2.prog_lang)
# print(dev_3.full_details())

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
