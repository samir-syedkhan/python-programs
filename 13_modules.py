'''
import calcy
result = calcy.add(10, 20)
print(result)

calcy.eve_or_odd(99)
'''
'''
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            return

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

# Run the calculator
calculator()
'''
import employees
#object creation
emp1 = employees.Employess('Samir', 'samir@gmail.com', 'Sales', 50000)
emp2 = employees. Employess("Faran", "faran@gmail.com", "DevOps", 10000)

emp1.emp_info()
emp2.emp_info()
emp1.change_dept('Marketing')
emp1.emp_info()
