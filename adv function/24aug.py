"""
opp has  4 pillar : 

1. inheritance 
    a.single  level inheritance
    b.multi level inheritance  
    c.multiple inhertitance 
    d.hiechical inheritance 
    e.hybrid inheritance 
2. encapsulation 
3. abstraction  
4. ploymorphism

"""

# inheritance  : one class access another class properties and method. 
"""
that allows a child class to reuse and extend attributes and methods from a parent class, promoting code reuse and cleaner design. 
"""

#ex :1 single level inheritance 

"""class student :  # -----> base class 
    name ="vraj"
    age =21    
    marks =89
    def display(self) :    #  keyword ----> class methods / attributes --->access 
        print("name is  : ",self.name)
        print("age is  :",self.age)
        print("marks is  :",self.marks)

class clg(student):   # clg ----> derived class
    clgname ="AU"
    
    def clg_name(self):
        print("clg name is  :",self.clgname)
        
c=clg()
c.display()
c.clg_name()
"""

# constructor  :  its automatically called when the object is created. 
"""
1. no return type  
2. constructor :  __init__  ------> constructor , special method
"""

# ex :2 
"""
class emp :
    def __init__(self):
        print("constructor is called")
        print("emp class")
        
e=emp()
"""
#non parameters  :
"""
class student :
    def __init__(self): 
        self.name =input("enter name : ")
        self.age=int(input("enter age : "))
        self.salary=int(input("enter salary : "))
        print("constructor is called")
    def display(self):
        print("name is ",self.name)
        print("age is ",self.age)
        print("salary is ",self.salary)
        
s=student()
s.display()
"""

# parameters  :

"""class student :
    def __init__(self,name,age,salary): 
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        print("name is ",self.name)
        print("age is ",self.age)
        print("salary is ",self.salary)
        
s=student("hetvi",22,30000)
s.display()
"""

# ex :2 multi level inheritance  vs  multiple  

""" 
class a                      class a 
class b(a)                   class b
class c(b)                   class c(b,a)


"""

# multi level : 


"""class emp : 
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        
class manager(emp):
    def __init__(self,m_name,m_salary,name,age,salary):
        emp.__init__(self,name,age,salary)  # constructor of emp class
        self.m_name=m_name
        self.m_salary=m_salary
    
    def display(self):
        print("employee name is ",self.name)
        print("employee age is ",self.age)
        print("employee salary is ",self.salary)
        
        print("*******manager details******")
        print("manager name is ",self.m_name)
        print("manager salary is ",self.m_salary)
        
class CEO(manager):
    ceo_name ="Patil Mital"
    
c=CEO("vraj",100000,"hetvi",21,60000)
print("ceo name is ",c.ceo_name)
c.display()
"""

# ex :3 hireachical inheritance
"""

class a 
class b (a)
class c(a)
class d(a)

"""

# ex :4 hybrid inheritance : combination  of one  or more  than one inheritance

"""
class a 
class b(a)
class c(a)
class d(b,c)
"""


