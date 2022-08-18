'''
    An iterable: is an object that can return an iterator. Any object with state that has an __iter__ method and returns
    An iterator: is an iterable. It may also be an object without state that implements a __getitem__ method. - The
    method can take indices (starting from zero) and raise an IndexError when the indices are no longer valid.

Python's str class is an example of a __getitem__ iterable.


    An Iterator: is an object that produces the next value in a sequence when you call next(*object*) on some object.
    Moreover, any object with a __next__ method is an iterator. An iterator raises StopIteration after exhausting the
    iterator and cannot be re-used at this pointer

'''
#* Iterating over entire iterable

s = {1, 2, 3}

#* get every element in s
for a in s:
 print (a) # prints 1, then 2, then 3

#* copy into list
l1 = list(s) # l1 = [1, 2, 3]

#* use list comprehension
l2 = [a * 2 for a in s if a > 2] # l2 = [6]


#* what can be ilterable
[1, 2, 3] # list, iterate over items
(1, 2, 3) # tuple
{1, 2, 3} # set
{1: 2, 3: 4} # dict, iterate over keys