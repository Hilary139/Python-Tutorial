'''

    Comments can be used to explain Python code.

    Comments can be used to make the code more readable.

    Comments can be used to prevent execution when testing code.

#This is a comment
print("Hello, World!")


'''


#* Variables
         #? A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
         #? A variable name must start with a letter or the underscore character
         #? A variable name cannot start with a number
         #? A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
         #? Variable names are case-sensitive (age, Age and AGE are three different variables)
#! Python has no command for declaring a variable.
x = 5
y = "Daniel"
print(x)
print(y)

x = 14       # x is of type int
x = "James" # x is now of type str
print(x)



#? Casting
#*If you want to specify the data type of a variable, this can be done with casting.

x = str(4)    # x will be '4'
y = int(5)    # y will be 5
z = float(6)  # z will be 6.0

#? Single or Double Quotes?
#? String variables can be declared either by using single or double quotes:

x = "John"
# is the same as
x = 'John'

#? Case-Sensitive
#? Variable names are case-sensitive.

a = 4
A = "Sally"
#A will not overwrite a


#? DATATYPES

'''

        In programming, data type is an important concept.

        Variables can store data of different types, and different types can do different things.

        Python has the following data types built-in by default, in these categories:

                    Text Type:	str
                    Numeric Types:	int, float, complex
                    Sequence Types:	list, tuple, range
                    Mapping Type:	dict
                    Set Types:	set, frozenset
                    Boolean Type:	bool
                    Binary Types:	bytes, bytearray, memoryview
                    None Type:	NoneType

#? To get the datatype
x = 5
print(type(x))

'''