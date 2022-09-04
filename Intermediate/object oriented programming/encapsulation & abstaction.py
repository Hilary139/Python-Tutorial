
#*ENCAPSULATION: is the mechanism of hiding of data implemenation... Means instance methods are kept private
#Example:
class SoftwareDeveloper():
#! Note using __salary (double underscore) makes it private so you can't access the salary value directly. but _salary would not throw an error.
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None
        self._num_bugs_solved = 10

# Getter
    def get_salary(self):
        return self._salary
# setter
    def set_salary(self, value):
        self._salary = value        

sd= SoftwareDeveloper('Max', 20)
print(sd.name, sd.age, sd._num_bugs_solved)

sd.set_salary(60000)
print(sd.get_salary())