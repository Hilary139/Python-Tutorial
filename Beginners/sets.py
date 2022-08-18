
#? Sets are used to store multiple items in a single variable.
#? Set items are unordered, unchangeable, and do not allow duplicate values.
#* simple example of a set here

set = {"hello", "world"}
print(set)

#* checking the type 
print(type(set))

#! Duplicates are not allowed in sets
#* example
set_items = {"one", "two", "three", "one", "two", "three"} 
print(set_items)


#* length of sets
print(len(set_items))
#! You'd notice that the output will be 3 istead of 6.. this is because sets dom't allow duplicates


#* datatypes
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"apple", True, 4} #todo: Sets can accept different datatypes

#* Accessing items in set
for x in set1:
    print(x)


#! Once a set is created, you cannot change its items, but you can add new items.
#* adding into a set.. We will add to the set2
set2.add(2)
print(set2)


#* removing an item from a set
set2.remove(2)


#* looping items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#* joining sets
#todo: you can use union(), intersetion(), update(), intersection_update(), symmetric_difference_update(), symmetric_difference() 

#? union()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#? update()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#? intersection_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


#? intersection() 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#? symentric_difference_update()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#? symmentric_difference

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


#?other set methods
'''
    add()	Adds an element to the set
    clear()	Removes all the elements from the set
    copy()	Returns a copy of the set
    difference()	Returns a set containing the difference between two or more sets
    difference_update()	Removes the items in this set that are also included in another, specified set
    discard()	Remove the specified item
    intersection()	Returns a set, that is the intersection of two other sets
    intersection_update()	Removes the items in this set that are not present in other, specified set(s)
    isdisjoint()	Returns whether two sets have a intersection or not
    issubset()	Returns whether another set contains this set or not
    issuperset()	Returns whether this set contains another set or not
    pop()	Removes an element from the set
    remove()	Removes the specified element
    symmetric_difference()	Returns a set with the symmetric differences of two sets
    symmetric_difference_update()	inserts the symmetric differences from this set and another
    union()	Return a set containing the union of sets
    update()	Update the set with the union of this set and others

'''