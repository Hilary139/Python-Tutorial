
#* Creating and working with Functions
'''
    Functions in Python provide organized, reusable and modular code to perform a set of specific actions. Functions
    simplify the coding process, prevent redundant logic, and make the code easier to follow. This topic describes the
    declaration and utilization of functions in Python.

'''
'''Python has many built-in functions like print(), input(), len().
Besides built-ins you can also create your own functions to do more specific jobs—these are called user-defined functions.'''

#*  Defining and calling simple functions
#? Using the def statement is the most common way to define a function in python. This statement is a so called single clause compound statement with the following syntax:
'''
def function_name(parameters):
         statement(s)

#?   function_name:
        is known as the identifier of the function. Since a function definition is an executable statement its
        execution binds the function name to the function object which can be called later on using the identifier.


#?   parameters:
        is an optional list of identifiers that get bound to the values supplied as arguments when the function is
        called. A function may have an arbitrary number of arguments which are separated by commas.

#?   statement(s): 
        - also known as the function body -  are a nonempty sequence of statements executed each time the
        function is called. This means a function body cannot be empty, just like any indented block.
 '''


#* Example: 
def func() :
    a = 2  #! They are local variables whivh can only be used within the function 
    b = 3
    print(a+b)    #This is a simple function declaration that adds local variables 'a' and 'b' and returns the result

func()    #todo: Calling back the function created above


#* That’s another example of a function definition which takes one single argument and displays the passed in value each time the function is called:
def name(fname) :
    print(fname)

name('Walter') #todo: Add a value to the function when the function is called 

#* adding 3 arguments to the function
def profile(fname, lname, age) : 
    print('My first name is ' + fname + '\nMy second name is ' + lname + '\nI am ' + str(age) + ' years old.') #! the print statement was concatinated with the '+' character

profile('Daniel', 'wash', 33) #! the function was contain 3 values for the function to run.. Not adding all the 3 values would throw an error

#? Parameters or Arguments?
#* The terms parameter and argument can be used for the same thing: information that are passed into a function.
'''
    From a function's perspective:

    A parameter is the variable listed inside the parentheses in the function definition.

    An argument is the value that is sent to the function when it is called. This

'''
#* To let a function return a value, use the return statement:
def function() :
    return 'Hello, World!'
print(function())   

#* function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def func() :
    pass

#todo: Practice more to understand above examples..  
