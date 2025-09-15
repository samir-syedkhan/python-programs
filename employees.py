
class   Employess:
    COMPANY = 'ABC.pvt.ltd'
    #constructor
    def __init__(self, name, email, dept, salary):
        self.name = name
        self.email = email
        self.dept = dept
        self.salary = salary

    def emp_info(self):
        print(f'name is {self.name}')
        print(f'salary is {self.email}')
        print(f'dept is {self.dept}')
        print(f'salary is {self.salary}')

    def change_dept(self, new_dept):
        self.dept = new_dept
        print(f'department changed to {new_dept}')


