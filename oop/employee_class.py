class Employee:
    """A simple employee class"""

    num_of_employees = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}.{self.last}@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)  

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


#inheritance
class Developer(Employee):
    raise_amt = 1.10

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

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())                



emp_1 = Employee('Lauren', 'Burwell', 70000)
dev_1 = Developer('Lauren', 'Burwell', 60000, 'python')
mgr_1 = Manager('Miranda', 'Priestly', 90000, [dev_1])


print(emp_1.fullname())
print(dev_1.prog_lang)
print(mgr_1.email)

mgr_1.print_emp()

print(isinstance(mgr_1, Manager))
print(issubclass(Manager, Developer))





