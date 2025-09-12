

user_list = [ "apple", "banana", "cherry", "watermelon", "pineapple" ]
print(user_list)
print(user_list[0])
print(user_list[1])
print(user_list[2])
print(user_list[3])
print(user_list[-1])
print(type(user_list))
user_list.append('mango')
user_list.insert(1, 'shanu')
del user_list[0]
print(len(user_list))
print(user_list)
d = [ "apple", "banana", "cherry", "watermelon", "pineapple" ]
# sorting of list items
d.sort()
d.sort(reverse=True)
d.reverse()
d.pop()
d.pop(0)
print(d)
d1 = [ "apple", "banana", "cherry", "watermelon", "pineapple" ]
print(d1[0:5]) #slicing


numeric_list = [ 1, 3 ,40, 59, 98,100, 549 ]
print(numeric_list)
print(min(numeric_list))
print(max(numeric_list))
print(sum(numeric_list))
