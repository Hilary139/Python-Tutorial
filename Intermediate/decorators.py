
#? A decorator is a design parttern in python that allows a user to add new functionality to an exiting object without modifying its structure
# types: function decorators and class decorators
#todo: They are called before defining a function.

#* examples: creating a decorator function to be used.
def decorate_func(func):

    def wrapper():
        print('start')
        func()
        print('end')   
    return wrapper


@decorate_func    # This is a decorator function
def name():
    print('alex')

name()    

   
