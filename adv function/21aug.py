"""
python  : object oriented programming language 
class :blue of print  of object
    
object : instance of class

ex : 

fruits :   ------> class
    apple banana orange  kiwi mango -----> object 

vehicle :  ----> class
    car bike motorbike  ------> object 

    
syntax :

class name :
    varibale  

a =class name()

"""

# ex 1 

"""class fruits:  # -----> class name 
    print("fruits")
    print("apple")
    print("banana")
    print("orange")
    print("kiwi")
    print("mango")

f=fruits()  # -----> f object of the fruits class 
"""
"""
types :

1.public class  : accessible from anywhere
2.private class : accessible from inside the class
3.protected class : accessible from inside the class and from subclasses (inheritance)

"""

# ex :2 
"""
class vehicle :   # class name ----->vehicle
    car_model="bmw"   # attributes ----> car_model,color,price
    price=4000000
    color = "black"

v=vehicle()  # -----> v object of the vehicle class
print("car model is ",v.car_model)
print("price is ",v.price)
print("color is ",v.color)

"""

# ex :3 
"""
class vehicle :   # class name ----->vehicle
    car_model="bmw"   # attributes ----> car_model,color,price
    price=4000000
    color = "black"

    def display(self):  # self ----> keyword to access the object ,and also attributes
        print("car model is ",self.car_model)
        print("price is ",self.price)
        print("color is ",self.color)

v=vehicle()  # -----> v object of the vehicle class
v.display()  # -----> calling the display function
print("car model is ",v.car_model)  # ----> object though access the class atrributes/variables
print("price is ",v.price)
print("color is ",v.color)
"""

# ex :4 public 

"""class employees :
    name="mital"  # name age  , salary is  public  ---> by default it taken public 
    age=21
    salary=30000

e=employees()
print("name is ",e.name)
print("age is ",e.age)
print("salary is ",e.salary)
e.name="hetvi"
e.age=22
e.salary=40000
print("after updation of name  age and salary  :")
print("name is ",e.name)
print("age is ",e.age)
print("salary is ",e.salary)
"""

# ex :5 private
"""
class employees :
    name ="mital"
    __age=21  # __  is private
    salary=80000 

    def display(self):
        print("age is ",self.__age)

e=employees()
print("name is ",e.name)
# print("age is ",e.__age)  # not  accessible  though object bcz age  is  private 
print("salary is ",e.salary)
e.display()
e.__age =90  # its not possible to change the age  bcz its private
e.display()
"""

# ex :6 bank 
"""
class bank :
    bank_name="HDFC"
    Branch= "naranpura"
    acc_no =729210001324 
    account_holder_name = "dishant dipakkumar shah"
    balance =25000 

    def deposit(self):
        deposit_amt =int(input("enter the amount to deposit : "))
        self.balance=self.balance+deposit_amt
        print("after  deposit amt is  ",deposit_amt)

    def withdraw(self):
        withdraw_amt =int(input("enter the amount to withdraw : "))
        if self.balance -withdraw_amt >=10000:
            self.balance=self.balance-withdraw_amt
            print("after  withdraw amt is  ",withdraw_amt)
        else :
            print("not enough balance you have to maintain the minimum balance of 10000")

    def check_balance(self):
        print("balance is ",self.balance)

    def display(self):
        print("bank name is ",self.bank_name)
        print("branch is ",self.Branch)
        print("account no is ",self.acc_no)
        print("account holder name is ",self.account_holder_name)
        print("balance is ",self.balance)
    

b=bank()
b.display()
b.deposit()
b.withdraw()
b.check_balance()"""