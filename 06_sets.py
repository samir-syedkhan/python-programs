# sets: unordered and unique elements. curly {} braces are used.

my_set = { 'mon', 'tue', 'wed', 'thu', 'fri' }
print(my_set)
print(len(my_set))
print(type(my_set))

my_set.add('sat')
print(my_set)

my_list = ['mon', 'tue', 'wed', 'thu', 'fri' , 'mon']
days_set = set(my_list) # list will be changed to set to have only unique values.
print(days_set)




