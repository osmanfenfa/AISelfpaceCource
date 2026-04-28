"""name = {"name": "Osman", 42: "Answer", "cat": "Caty"}
print(name)
print(list(name.keys()))
print(list(name.values()))
print(list(name.items()))
print(type(name))
print(name['name'])

name2 = {True: True}
print(type(name2))
print(name2[True])

name3 = {True: 'yes', False: 'no'}
print(name3[True])
print(name3[False])


name4 = {'name': 'Osman' 'Tamba', 'color': 'red'} #== {'color': 'red', 'name': 'Osman' 'Tamba'}
print(name4)
print(list(name4.values()))

name5 = {"name": "Osman"} == {"Osman": "name"}
print(name5)

name6 = {"password": "1234"} == {"password": "1234"}
print(name6)"""


spam = {'name': 'Fenfaquee', 'color': 'red'}
spam.get('colors')
spam.get('colors', 'red')
spam.setdefault('name', 'Fenfaquee')
print(spam)

name7 = {}
name7['fruit'] = 'apple'
print(name7)
name7['fruit'] = 'banana'   # same key again
print(name7)