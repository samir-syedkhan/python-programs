# for loop exaple codes
'''
for i in 1, 2, 3, 4, 5:
    #print('samir')
    print(i)
'''
'''
user_list = [ 'Alex', 'Raju', 'Subhan', 'jamal']   #for loop with list
for user in user_list:
    print(user)
'''
#age_info = {'Salim': 25, 'shalim': 32}
#for name, age in age_info:
#    print(name, age)

marks = {
    'Hindi': 80,
    'English': 70,
    'Science': 60
}

for subject, marks in marks.items():
    print(f'Subject is: {subject}')
    print(f'Marks are: {marks}')

    for num in range(10):
        print(num)
        

