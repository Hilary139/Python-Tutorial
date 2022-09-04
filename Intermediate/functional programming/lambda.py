#lambda Functions
#? The lambda keyword creates an inline function that contains a single expression. The value of this expression is what the function returns when invoked.

#* Example
morning = lambda : 'Good Morning from a lambda function'  #todo:Note everything is in a single line
print(morning()) 

#* Regular function
def greet ():
    print('Good Morning from regular python function')
greet()    
#! Note the differene between them... The regular function includes more lines, while lamda  function uses a single line..

#* Taking arguments within a lamda function
# Uppercase arguments
uppercase_text = lambda y : y.upper()
print(uppercase_text("Hello, world!"))

#* They can also take arbitrary number of arguments / keyword arguments, like normal functions
greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
greeting('hello', 'world', world='world')




