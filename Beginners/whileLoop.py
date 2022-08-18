
#? With the while loop we can execute a set of statements as long as a condition is true.

#* example 
i = 1 
while i <= 10:
    print(i)
    i += 1
#todo: The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.


#* With the break statement we can stop the loop even if the while condition is true:
x = 1
while x == 2:
    print(x)
    if x == 4:
        break
    x += 1


#* With the continue statement we can stop the current iteration, and continue with the next:
y = 0
while y <= 2:
    print(y)
    if y == 2:
        continue
    x += 10
    break

#* with the else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#* with the pass statement
i = 1
while i < 6:
   
   pass
# end while