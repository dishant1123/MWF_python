# local variable :

"""def fun():
    x=100   # x local variable  : only access in function 
    print(x)
    
fun()
# print(x)  # note : it's local variable  so you can't access outside the  function
"""

# global variable :
"""x=100 

def func():
    print(x)  # global variable access any where  in side function  and outside the  function
func()
print(x)  # global variable can access outside the  function.

"""

# global variable  modify : global key word 
"""y=800 

def func():
    global y 
    y=900 
    print(y)
func()
print(y)
"""

# create , login  : 

"""
create : enter the  username : d123 
         enter  the  passowrd :d@123
         
login : 

"""
username =""
password =""

def create():
    username = input("enter the  username : ")
    password = input("enter  the  passowrd :")
    
