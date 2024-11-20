my_dict = {'Egor':2000 ,'Angelina':1999 , 'Olga': 1970}
print(my_dict)
print(my_dict['Egor'])
my_dict.update({'Max':1980 , 'Elena':1970})
print(my_dict)
del my_dict['Angelina']
print(my_dict.get('Angelina'))
print(my_dict)

my_set = {100,101,101,103,105,103}
print(my_set)
my_set.update({'urban' , 'tor'})
print(my_set)
print(my_set.discard(101))
print(my_set)