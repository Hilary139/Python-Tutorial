
#? Object oriented programming
'''
        Python offers itself not only as a popular scripting language, but also supports the object-oriented programming
        paradigm. Classes describe data and provide methods to manipulate that data, all encompassed under a single
        object. Furthermore, classes allow for abstraction by separating concrete implementation details from abstract
        representations of data.
'''

'''
        The class is made up of attributes (data) and methods (functions).
        2. Attributes and methods are simply defined as normal variables and functions.
        3. As noted in the corresponding docstring, the __init__() method is called the initializer. It's equivalent to the
        constructor in other object oriented languages, and is the method that is first run when you create a new
        object, or new instance of the class.
        4. Attributes that apply to the whole class are defined first, and are called class attributes.
        5. Attributes that apply to a specific instance of a class (an object) are called instance attributes. They are
        generally defined inside __init__(); this is not necessary, but it is recommended (since attributes defined
        outside of __init__() run the risk of being accessed before they are defined).
        6. Every method, included in the class definition passes the object in question as its first parameter. The word
        self is used for this parameter (usage of self is actually by convention, as the word self has no inherent
        meaning in Python, but this is one of Python's most respected conventions, and you should always follow it).
        7. Those used to object-oriented programming in other languages may be surprised by a few things. One is that
        Python has no real concept of private elements, so everything, by default, imitates the behavior of the
        C++/Java public keyword. For more information, see the "Private Class Members" example on this page.
        8. Some of the class's methods have the following form: __functionname__(self, other_stuff). All such
        methods are called "magic methods" and are an important part of classes in Python. For instance, operator
        overloading in Python is implemented with magic methods.
'''
#* Example usage
class Book(): #* class block
    def __init__(self, title, pages, author):  #* class initializer
        #* Instance attributes
        self.title = title #* class variale 
        self.pages = pages #* class variale
        self.author = author #* class variale

#* Creating instances 
book_one = Book("Rich dad poor Dad", 5000, "Richy fang ") #* Adding arguments to the parameter
book_two = Book("Diary of a wimpy kid", 300, "hadly jeff") #* Adding arguments to the parameter
print(book_one.title, book_one.pages, book_one.author)  #* Print the title, the pages, and the author
print(book_two.title, book_two.pages, book_two.author)  #* Print the title, the pages, and the author
#? The above example creates a book class that has parameters for title, author and pages. And you can call it and pass different arguments.


#* Another class example..
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
person_one = Person("Emmanuel", 11)
print(person_one.name, person_one.age)        
        

#* Another example
class Student():
    def __init__(self, name, department, age):
        self.name = name
        self.department = department
        self.age = age
student_one = Student('My Name is: John Jones\n', 'Department is: Computer Science\n', 'My age is 23\n')   
print(student_one.name, student_one.department, student_one.age)     


#todo: 4 principles of Object Oriented Programming
#* Inheritance
#* Polymorphism
#* Encapsulation
#* Abstraction

#todo: PRACTICE with more examples
class Store_staff():

        # class attributes
        notice = "Late coming isn't allowed!!"


        def __init__(self, name, department, age, job_title, job_description):
                self.name = name
                self.department = department
                self.age = age
                self.job_title = job_title
                self.job_description = job_description

first_staff = Store_staff('Lisa', 'finance', 30, 'Financial Manager', ' Managing finances')                
print(Store_staff.notice)
print(first_staff.name, first_staff.department, first_staff.age, first_staff.job_title, first_staff.job_description)
        