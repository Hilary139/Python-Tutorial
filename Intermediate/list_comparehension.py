
#? list comparihension offers a shorter syntax when you create a new list based on the values of an existing list

#* example (normal method)
cars = ['bmw', 'audi', 'jeep', 'benz']

for x in cars:
    if 'audi' in x :
        #print(cars[1])
        #or
        print(x)

#* list comparism 
compare = [x for x in cars if 'bmw' in x ] 
print(compare)       

#todo: note the difference..

#* to ilterate the list is even easier
ilterate = [x for x in cars]
print(ilterate)

#* using normal method
'''
for x in cars :
   print(cars)
'''   

#? YOU CAN ALSO DO THIS WITH THINGS LIKE SET, TUPLE DICTIONARY.