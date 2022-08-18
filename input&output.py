
#? Using the print function

def print_function(message):
    print(message)

#*  Input from a File    
#todo: Input can also be read from files. Files can be opened using the built-in function open. Using a with <command> as <name> syntax (called a 'Context Manager') makes using open and getting a handle for the file super easy:
#* This example shows how to write a file.. First we create a file inside the directory then using the 'w': which is for writting inside the file created.
with open ('testingFile.txt', 'w') as file :
    file.write('This file is being generated from input&otput.py file.\n')
    file.write('Fish\nMeat\nChicken')

#* Reading a file from a directory.. We will use the built-in function 'r' to read
with open('testingFile.txt', 'r') as file :
    content = file.read()
    print(content)

#* We will use the built-in function 'rb'
with open('testingFile.txt', 'rb') as fileobj:
 print(type(fileobj.read())) # <class 'bytes'>


#* The simplest way to iterate over a file line-by-line:
with open('testingFile.txt', 'r') as File_loop :
    for line in File_loop :
       print(line)



#* Using Input() for python 3.x  and python 2.x is raw_input() 
user_number = input("input a number: ")
# user_number_2x  = raw_input("input a number: python2.x") #! This will throw an error because i'm running python 3.x and above.

'''
#? There are different modes you can open a file with, specified by the mode parameter. These include:
            'r' - reading mode. The default. It allows you only to read the file, not to modify it. When using this mode the
            file must exist.
            'w' - writing mode. It will create a new file if it does not exist, otherwise will erase the file and allow you to
            write to it.
            'a' - append mode. It will write data to the end of the file. It does not erase the file, and the file must exist for
            this mode.
            'rb' - reading mode in binary. This is similar to r except that the reading is forced in binary mode. This is
            also a default choice.
            'r+' - reading mode plus writing mode at the same time. This allows you to read and write into files at the
            same time without having to use r and w.
            'rb+' - reading and writing mode in binary. The same as r+ except the data is in binary
            'wb' - writing mode in binary. The same as w except the data is in binary.
            'w+' - writing and reading mode. The exact same as r+ but if the file does not exist, a new one is made.
            Otherwise, the file is overwritten.
            'wb+' - writing and reading mode in binary mode. The same as w+ but the data is in binary.
            'ab' - appending in binary mode. Similar to a except that the data is in binary.
            'a+' - appending and reading mode. Similar to w+ as it will create a new file if the file does not exist.
            Otherwise, the file pointer is at the end of the file if it exists.
            'ab+' - appending and reading mode in binary. The same as a+ except that the data is in binary. The same async
'''

'''
#?  Python 3 added a new mode for exclusive creation so that you will not accidentally truncate or overwrite and existing file.
            'x' - open for exclusive creation, will raise FileExistsError if the file already exists
            'xb' - open for exclusive creation writing mode in binary. The same as x except the data is in binary.
            'x+' - reading and writing mode. Similar to w+ as it will create a new file if the file does not exist. Otherwise,
            will raise FileExistsError.
            'xb+' - writing and reading mode. The exact same as x+ but the data is Binary instead
'''