
#? For loops 

#* example:
for_list = [2,4,4,6,7,]
for x in for_list :
    print(x)

#* Using the range function
for i in range(6) :
    print(i)


#* With the break statement we can stop the loop even if the for condition is true:
fruits = ["apple", "banana", "Orange"]
for x in fruits:
  print(x)
  if x == "banana":
    break    

#* ith the continue statement we can stop the current iteration, and continue with the next:
fruits = ["Mango", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


  #* Else if in the For loop
for x in range(6):
     print(x)
else:
  print("Finally finished!")


#* Nested for loop 
city = ["toronto", "lagos", "accra"]
country = ["canada", "nigeria", "ghana"]

for x in city:
  for y in country:
    print(x, y) 


#* The pass statement
for x in city:
    pass   