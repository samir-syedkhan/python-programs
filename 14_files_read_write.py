
#with open('user.info', 'w') as file:
 #   file.write('This is my first text file using python')

with open('user.info', 'r') as file:
     content = file.readlines()
for line in content:
     print(f'Welcome {line.rstrip()}')