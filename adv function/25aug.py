# encapuslation  : 
"""
Encapsulation is one of the four main principles of Object-Oriented Programming (OOP). It means wrapping data (variables) and methods (functions) into a single unit (class) and restricting direct access to some of the object's data.

Python does not have truly private variables, but it uses naming conventions to indicate access levels.


2 method : 

1. get   method : data  get,retieve  -----> collect 
2. set   method : update  
"""

# ex :1 

class employees :
    def __init__(self) :
        self.name ="vraj"
        self.__age =21 
        self.__salary =100000

    def get_age(self):
        return self.__age
    
    def get_salary(self):
        return self.__salary
    
    def display_name(self):
        print("name is ",self.name)

    def set_salary(self,new_salary):
        self.__salary=new_salary

    def set_age(self,new_age):
        self.__age=new_age

e=employees()
print("private data members using  get  method :")
print("age is ",e.get_age())
print("salary is ",e.get_salary())

print("private data members using  set  method :")
e.set_age(20)
e.set_salary(80000)

print("after using set method :")
print("age is ",e.get_age())
print("salary is ",e.get_salary())

"""
Why Use Encapsulation?
Data Hiding: Prevents direct modification of sensitive data.
Security: Controls how data is accessed or modified.
Maintainability: Makes code easier to update and debug.
Validation: Allows checking data before changing it.
"""