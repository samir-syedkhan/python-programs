#dictionaries key:value curly braces {} are used.

marks = {'English': 80,
         'Math': 90,
         'science': 70 }
print(marks['English'])
print(marks['Math'])
print(marks['science'])
print(type(marks))
print(marks.get('English'))
print(marks.get('bio')) # will give None instead of an error if key is not available.

marks['bio'] = 100 # to add it to the dictionary
print(marks)
del marks['science'] # to delete science.
print(marks)
print(len(marks))

'''
car = {'brand': 'Ford', 'model': 'Q3' }
print(" Brand of a car is " + car['brand'] )

print(" model of a car is " + car['model'])
'''


