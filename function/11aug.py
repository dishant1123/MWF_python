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
    
    global username,password
    username = input("enter the  username : ")
    password = input("enter  the  passowrd :")
    
    print("username : ",username)
    print("password : ",password)
    print("create success")
    
def login():
    attempt = 3 
    while attempt > 0 :
        user =input("enter the  username : ")
        passw=input("enter  the  passowrd :")
    
        if user==username and passw==password:
            print("login success")
            return True
        else :
            attempt -= 1
            print("try again")
    
    password = ""
    username = ""
    return False


while True:
    print("1.create")
    print("2.login")
    print("3.exit")
    choice = int(input("enter your choice : "))
    
    if choice==1:
        create()
    
    elif choice==2:
        if username=="" or password=="":
            print("please create first")
        else :
            login()
    elif choice==3:
        break
    