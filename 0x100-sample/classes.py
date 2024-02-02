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
        return self.pay * Employee.raise_amt


emp_1 = Employee("john", "Doe", 50000)
emp_1.raise_amt = 1.2

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(int(emp_1.apply_raise()))
