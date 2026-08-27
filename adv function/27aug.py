#polymorphism : many forms of same function
"""
Polymorphism means "many forms." In Python, polymorphism allows the same method, function, or operator to work differently depending on the object it is used with.

1. method overriding
2. method overloading

"""

# ex :1 function  overriding 

"""def length(a):
    return len(a)

print(length([1,2,3,4,5]))
print(length("hello mital !!!!! how  are you"))
print(length((1,2,3,4,5)))
print(length({1,2,3,4,5}))
"""
# ex :2  class method overriding

"""class animal:
    def speak(self):
        print("animal speak")

class cat(animal):
    def speak(self):
        print("meowwwwww .......meowwwww")

class dog(animal):
    def speak(self):
        print("bhaseee  .....bhowwwww")

class bird(animal):
    def speak(self):
        print("chirp ....chirp")

c=cat()
c.speak()
a=[cat(),dog(),bird()]
for i in a:
    i.speak()
"""

# ex :3 operator overloading

"""def add(a,b):
    return a+b

print(add(90,67))
print(add(90.0,67.0))
print(add("mital","patil"))
print(add(1j,2j))
"""

# ex :4 constructor overloading :

"""class student :
    def __init__(self):
        print("constructor")

    def __init__(self):
        print("constructor of  student")

    def display(self):
        print("hetvi")

    def display(self):
            print("vraj- team leader")

s=student()
s.display()
"""

# ex :5 

"""class calculator:

    def add(self,a,b=0,c=0):
        return a+b+c
   
c=calculator()
print(c.add(1,2,3))
print(c.add(1,2))
print(c.add(1))
print(c.add(90,90))
"""

# 2 method  :
"""
1. class method :
---> use  a cls 
---> direct access to the  class name 
---> you can change using cls 
"""

"""class college:
    clg_name ="Nirma University"

    @classmethod   # ---->decorator 
    def display(cls,new_name):
        cls.clg_name=new_name
        print(cls.clg_name)

# college.display("AU")
print(college.clg_name)
college.display("AU")
print(college.clg_name)"""

# static method :
"""
----> work like  normal function 
----> no need to use  self
----> no need to use  cls
----> no change though the  cls
"""

"""class stdennt :
    name="mital"
    age=21 
    clg="Ahmedabad University"

    @staticmethod    # decorator
    def display():
        print(stdennt.name)
        print(stdennt.age)
        print(stdennt.clg)

s=stdennt()
s.display()
s.name="hetvi"  # not changes in static  method 
s.display()
"""

# abstraction : to hide the details of the implementation
"""
Definition:
Abstraction means hiding unnecessary implementation details and showing only the essential information to the user.

Real-life example

When you use an ATM, you know how to:

Insert a card
Enter PIN
Withdraw money

But you don't need to know how the ATM internally communicates with the bank.
That is abstraction — you see what to do, not how it works internally.

ex :1   real life example : driving car but  we don't know how car work ,how to engine work ,how to transmission work ....

from abc import ABC  -----> abstract base class 

note : you can't create object of abstract class.
"""

from abc import ABC,abstractmethod

class bank(ABC):
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.balance =0

    @abstractmethod
    def deposit(self,amount):
        pass 

    @abstractmethod
    def withdraw(self,amount):
        pass

    def display(self):
        print("name :",self.name)
        print("address :",self.address)
        print("balance :",self.balance)

class saving_account(bank):
    def __init__(self,name,address,interest_rate):
        bank.__init__(self,name,address)
        self.interest_rate=interest_rate
        self.balance =0

    def deposit(self,amount):
        self.balance +=amount
        print("deposited amount :",amount)

    def withdraw(self,amount):
        self.balance -=amount
        print("withdraw amount :",amount)

s=saving_account("mital","ahmedabad",5)
s.deposit(1000)
s.withdraw(100)
s.display()