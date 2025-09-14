'''
# Creating a function
def greeting(user_name, *hobbies):
    print("*" * 30)
    print(f"Hello {user_name}!")
    print("hobbies are:")
    for hobby in hobbies:
        print(f' - {hobby}')
    print(f"Hobby is {hobbies}.")
    print("Welcome to the Linux world!")
    print("*" * 30)

# Calling the function
greeting('Samir', 'football', 'shooting', 'tech')
greeting('Aziz', 'cricket')
greeting('Saleem', 'singing' )
'''


'''
def greeting(user_name, age, **other_info):
    print("*" * 30)
    print(f"Hello {user_name}!")
    print("Thank you for signing in:")
    print("*" * 30)

greeting('Samir', age=30, city='islamabad', email='samir@gmail.com')
greeting('Saleem', age=28, city='peshawar')
greeting('Aziz', age=31, city='hangu')
'''

def add (num1, num2):
    return num1 + num2
print(add(10, 20))
