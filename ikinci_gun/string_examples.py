#https://GoalKicker.com/PythonBook
#kitabından calisma

x = 'bu'
y = 'bir'
z = ' birlestirme'
q = 'cümlesi'

print('{} {} {} {}'.format(x,y,z,q))
print(f'{ x} { y}')

my_list = ['zero', 'one', 'two']
print("second element is {[1]}".format(my_list))

print('{0:.0f}'.format(42.12345))
print('{0:.1f}'.format(42.12345))

data = {'first': 'Hodor', 'last': 'Hodor!'}
print('{first} {last}'.format_map(data))
print('{first} {last}'.format(first='Hodor', last='Hodor!'))

#getitem:
person = {'first': 'arthur', 'last': 'police'}
print('{p[first]} {p[last]}'.format(p=person))

#getattr:

class Person(object):
    ad = 'neville'
    job = 'artist'

print('{d.ad} {d.job}'.format(d=Person()))

print(str.upper('this is a string!'))


