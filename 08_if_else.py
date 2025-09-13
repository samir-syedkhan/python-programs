#if-else condition 

if 10>8:
    print('True')
else:
    print('False')


print('Enter a no. and check if it is even or odd')
num = int(input('Enter a no -'))
if num % 2 == 0:
    print('Even')
else:
    print('Odd')


users = ['paul', 'raju', 'kim']
if 'paul' in users:
    print('User exists')
else:
    print("User doesn't exist")


marks = int(input('Enter marks: -'))
if marks >= 80:
    print('A Grade')
elif marks >= 70:
    print('B Grade')
elif marks >= 60:
    print('C Grade')
else:
    print('Fail')


age = 20
voter_id = True
if age >= 18:
    if voter_id:
        print('You can vote')
    else:
        print('Please apply for a voter id first')

else:
    print('You can\'t vote')


age = 20                    # using operator
voter_id = True
if age >= 18 and voter_id:
    print('You can vote')
else:
    print('You cannot vote')
