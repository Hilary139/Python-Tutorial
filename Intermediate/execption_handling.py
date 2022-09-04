
#? Exception handling for catching errors in your program
'''
try: lets you test a block of code for errors

except: lets you handle the error

else: lets you execute code when there is no error

finally: lets you execute code regardless of the result of the try- and except blocks.
'''

#* example

try: 
    print(x)
except: 
    print('An exception occurred')    


#* You can try many exceptions 
# example 
try :
    print(x)
except NameError:
    print('An exception occurred')
except:
    print('something went wrong')            



#*using the else    
try: 
    print('Try me!')
except:
    print('something went wrong')
else:
    print('Nothing went wrong')    


#* using finally
try: 
    print('Tried me finally!')
except:
    print('something went wrong')
finally:
    print('Nothing went wrong Finally')    

'''
#* using all the exceptions 
try: 
   f = open('testingFile.txt')
   try:
     f.write('Trying out exception')
   except:
    print('Something went wrong from the exception_handling file')
   finally:
    f.close()
except:
    print('Something went wrong')             
#! This will throw an error because we are trying to write a file that is not writabale
'''


#* Rasing exception
'''You can choose to throw an exception if a condition occurs'''
#* WE USE THE (raise) KEYWORD TO THROW AN EXCEPTION
x = 2
if x > 4:
    raise Exception('Invalid, The number is not greater than 4')

x = 2
if x > 4:
    raise TypeError('Invalid, The number is not greater than 4')    