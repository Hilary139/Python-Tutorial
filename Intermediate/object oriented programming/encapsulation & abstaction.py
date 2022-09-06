
#*ENCAPSULATION: is the mechanism of hiding of data implemenation... Means instance methods are kept private
#Example:
class SoftwareDeveloper():
#! Note using __salary (double underscore) makes it private so you can't access the salary value directly. but _salary would not throw an error.
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None
        self._num_bugs_solved = 0


    def code(self):
        self._num_bugs_solved +=1    

# Getter
    def get_salary(self):
        return self._salary
# setter
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)

# Abstraction
    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2 
        return base_value * 3        
    
sd= SoftwareDeveloper('Max', 20)
print(sd.name, sd.age, sd._num_bugs_solved)

for i in range(70):
    sd.code()

sd.set_salary(60000)
print(sd.get_salary())

