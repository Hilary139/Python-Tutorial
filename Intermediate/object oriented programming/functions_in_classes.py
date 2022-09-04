
#? Adding Functions to classes (Object oriented programming)

#* lists 
list_item =["harry", "john", "gary"]
list_item_two = ["Apple", "Microsoft", "IBM"]


'''
def func(se):
        print(f"{se[2]} is in the right position... ") #* this line get's the right position from the list
se(list_item_two)        
'''

#* examples
class Func_in_classes():
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

    #* function instance method
    def code(self):
        print(f"{self.name} is a programmer... ")

    def job(self):
        print(f"{self.name} is a {self.job_title}")    

    def code_in_lang(self, language):
        print(f"{self.name} is a {self.job_title} and writes code in {language}")

    #? using the __str__ method
#* examples using the __str__ method
    def __str__(self):
        info = f'name = {self.name}, job = {self.job_title}'
        return info 

#* outputing the values of each class defined above
name_func = Func_in_classes('james', 'software engineer' )
name_str = Func_in_classes('Hilary', 'creator of the repo')
name_func_two = Func_in_classes('silver', 'lawyer' )

#* calling them
name_func.code()
name_func_two.job()
name_func.code_in_lang('python')

#* calling from the __str__ method
print(name_str)
 

