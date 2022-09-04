
#* INHERITANCE: process one class takes on the attribute and methods of another class

# Inherits, extends, override
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    
    def Works(self):
        print(f"{self.name} is working...")


class SoftwareDeveloper(Employee):
    #* extending the employee status for a software engineer
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary) #* this initializer is used to get the name, age and salary from the employee class
        self.level = level

    def Debug(self):
        print(f"{self.name} is debugging..")    

#! This overrides the default implementation from the employee class
    def Works(self):
        print(f"{self.name} is coding...")
     


class Designer(Employee):
#! This overrides the default implementation from the employee class
    def Works(self):
        print(f"{self.name} is designing...")

    def Draw(self):
        print(f"{self.name} is drawing..")    


sd = SoftwareDeveloper('harry', 30, 200000, 'jnr') # software developer arguments
#print(sd.name, sd.age) # prints the software developer
#sd.Works()
sd.Debug()
print(sd.level)

de = Designer('dan', 22, 100000) # designer arguments
#print(de.name, de.age) # prints the designer arguments
#de.Works()
de.Draw()



#* POLYMOPHISM: meaning Many shapes

# Example 
employees = [SoftwareDeveloper('Gray', 20, 300000, 'junior'),
             SoftwareDeveloper('Styles', 24, 500000, 'Senior'),
             Designer('Brad', 50, 200000)]

def motivate_employees(employees):
    for employee in employees:
        employee.Works()

motivate_employees(employees)        