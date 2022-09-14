
#* heapq module
''' To find the largest items in a collection, heapq module has a function called nlargest, we pass it two arguments, the
first one is the number of items that we want to retrieve, the second one is the collection name '''

import heapq

#* Examples: Getting largest number from the list
num_list = [2,44,55,234,456,67,101,123,478,1,55,6,7,90]
heapq_largest = heapq.nlargest(3, num_list)
print('Getting the largest number from the list ' + str(heapq_largest))


#* Getting th smallest number from the list
heapq_smallest = heapq.nsmallest(4, num_list)
print('Getting the smallest number from the list ' + str(heapq_smallest))

#* Examples: Getting the largest and smallest age from the dictionary
people = [
 {'firstname': 'John', 'lastname': 'Doe', 'age': 30},
 {'firstname': 'Jane', 'lastname': 'Doe', 'age': 25},
 {'firstname': 'Janie', 'lastname': 'Doe', 'age': 10},
 {'firstname': 'Jane', 'lastname': 'Roe', 'age': 22},
 {'firstname': 'Johnny', 'lastname': 'Doe', 'age': 12},
 {'firstname': 'John', 'lastname': 'Roe', 'age': 45}
  ]
#* Getting the smallest age from the dictionary
heapq_dict_smallet = heapq.nsmallest(2, people, key=lambda x: x['age'])
print('Getting the smallest ages from the dictionary ' + str(heapq_dict_smallet))


#* Getting the largest age from the dictionary
heapq_dict_largest = heapq.nlargest(2, people, key=lambda y: y['age'])
print('Getting the largest age from the dictionary ' + str(heapq_dict_largest))


#* Popping and heapifying the list
list_box = [33,4,55,6,77,8,44]
heapq_pop = heapq.heappop(list_box)
print('Pops a number in th list box ' + str(heapq_pop))
#! The most interesting property of a heap is that its smallest element is always the first element: heap[0]

list_box_heap = [33,4,55,6,77,8,44]
heapq_heapify = heapq.heapify(list_box_heap)
print('Heapify a number in th list box ' + str(heapq_heapify))

#* Getting the largest and smallest from the range
heapq_range_small = heapq.nsmallest(3, range(20))
print('getting the smallest value from the range ' + str(heapq_range_small))

heapq_range_large = heapq.nlargest(7, range(70))
print('getting the largest value from the range ' + str(heapq_range_large))



'''
#* Here is a program that extracts 1000 longest lines from a file:
     
      with open(filename) as f:
 longest_lines = heapq.nlargest(1000, f, key=len)

'''