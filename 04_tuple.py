# tuple is immutable.....value can not be changed
days = ( 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'mon' )
print(days)
print(len(days))
print(type(days))
print(days[0])
#days[1] = 'fri'   error will raise as tuple object can't be changed.
print(days.count('mon'))
print(days.index('mon'))


