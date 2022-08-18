'''
#? Python supports the usual logical conditions from mathematics:

        Equals: a == b
        Not Equals: a != b
        Less than: a < b
        Less than or equal to: a <= b
        Greater than: a > b
        Greater than or equal to: a >= b

'''
'''
#todo:  Indentation:
      Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

'''




#* An "if statement" is written by using the if keyword.
example = 3
if 5 > example:
    print("the example value is " + str(example))

#*  without indentation 
a = 33
b = 200
c = 300
d = 400
#if b > a:
#print("b is greater than a") #! you will get an error

#* The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
if a > b :
    print("It is greater than")
elif a < b :
    print("It is less than")  


#* The else keyword catches anything which isn't caught by the preceding conditions.
if a == b :
    print("equal to")
elif a > b :
    print("greater than") 
else: 
    print("less than")            


#* The and keyword is a logical operator, and is used to combine conditional statements:
if a > b and c < d :
    print("Both conditions are true")


#* The or keyword is a logical operator, and is used to combine conditional statements:
if a > b or c < d :  
    print("Both conditions are false")

#* Nested if statements    
if a > c :
    print("Greater")
    if d == b :
        print("equal")
    else: 
        print("None!")

#* if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
if b == c :
    pass


