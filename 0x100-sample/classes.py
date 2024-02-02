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
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_strs):
        first, last, pay = emp_strs.split('-')
        return cls(first, last, int(pay))
    
    @staticmethod
    def is_week_day(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True
    

    
# Creating instance from the Employee Class
emp_1 = Employee("john", "Doe", 50000)
emp_2 = Employee('Jane', 'Doe', 35000)

# setting or changing the pay
emp_1.set_raise_amt(1.05)

#New employee strings 
emp_str_3 = 'Corey-Schafer-60000'
emp_str_4 = 'Mike-Adenuga-80000'

# Using the class method to create new instances
# emp_3 = Employee.from_string(emp_str_3)
# print(type(emp_3.pay))
# print(int(emp_3.apply_raise()))

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(int(emp_1.apply_raise()))

from datetime import date
my_date = date(2024,2,3)
day = Employee.is_week_day(my_date)
print(day)