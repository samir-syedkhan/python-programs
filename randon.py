import random
'''
print(random.random())
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.uniform(3.5, 6.5))

fruits = ['apple', 'banana', 'orange', 'mango', 'pineapple']
print(random.choice(fruits))
print(fruits)
print(random.shuffle(fruits))
print(fruits)
'''

while True:
    print(f'Number is {random.randint(1, 6)}')
    user_input = input('Do you want to continue? (y/n): ')
    if user_input == 'n':
        break

