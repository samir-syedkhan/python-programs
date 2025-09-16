'''
try:
    print(10/0)
except ZeroDivisionError:
    print("Kindly do  not divide by zero")
print(10 + 2)
print(30 - 20)
'''
'''
try:
    with open('user_info.txt', 'r') as file:
        content = file.readlines()
except FileNotFoundError:
    print("File not found")
else:
    for line in content:
        print(f'Wlcome to {line.rstrip()}')
'''
try:
    with open('user_info.txt', 'r') as file:
        content = file.readlines()
except Exception as e:
    print(e, type(e))
else:
    for line in content:
        print(f'Wlcome to {line.rstrip()}')
finally:
    print('DB closed')
print('Lines after exception handling')