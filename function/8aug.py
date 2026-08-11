"""
function  : 

1. no arg  no return 
2. with  arg  no return 
3. no arg  with return 
4. with arg with return 
"""

# no arg  with return 

"""def add():
    a=int(input("enter the a value :"))
    b=int(input("enter the b value :"))
    c=a+b 
    return c 

print(add())
"""

# with arg  with return

"""def add(a,b):
    return a+b 

print(add(34,56))
print(add(34.89,56.90))
print(add("mital",'patil'))
"""

"""l1 =[121,123,456,89] 
l2=[]

for i in l1 :   # 123
    result =str(i)[ : : -1]  # result = "321" 
    l2.append(int(result))   # l2.append(121)
print(l2)
"""
# ex : 1 no arg  no return 
"""
def reverse_list():
    l1 =[121,123,456,89] 
    l2=[]

    for i in l1 :   # 123
        result =str(i)[ : : -1]  # result = "321" 
        l2.append(int(result))   # l2.append(121)
    print(l2)
reverse_list()
"""

# ex : 2 with arg  no return

"""
def reverse_list(l1):
   
    l2=[]

    for i in l1 :   # 123
        result =str(i)[ : : -1]  # result = "321" 
        l2.append(int(result))   # l2.append(121)
    print(l2)
reverse_list( l1 =[121,123,456,89] )
"""

# ex 3 : no arg  with return

"""def reverse_list():
    l1 =[121,123,456,89]
    l2=[]

    for i in l1 :   # 123
        result =str(i)[ : : -1]  # result = "321" 
        l2.append(int(result))   # l2.append(121)
    return l2
print(reverse_list())
"""

# ex :4 with arg  with return
"""
def reverse_list(l1):
    l2=[]

    for i in l1 :   # 123
        result =str(i)[ : : -1]  # result = "321" 
        l2.append(int(result))   # l2.append(121)
    return l2
print(reverse_list([121,123,456,89]))
"""

# menu driven  program  calculator  

def add(a,b) :
    return a+b

def sub(a,b) :
    return a-b

def mul(a,b) :
    return a*b

def div(a,b) :
    return a/b

def mod(a,b) :
    return a%b

while True :
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. modulus")
    print("6. exit")
    
    choice=int(input("enter the choice :"))
    
    if choice ==6 :
        print("thanks for using the calculator")
        break
    
    num1=int(input("enter the first number :"))
    num2=int(input("enter the second number :"))
    
    if choice==1 :
        print(num1,"+",num2,"=",add(num1,num2))
    
    elif choice==2 :
        print(num1,"-",num2,"=",sub(num1,num2))
    
    elif choice==3 :
        print(num1,"*",num2,"=",mul(num1,num2))
    
    elif choice==4 :
        print(num1,"/",num2,"=",div(num1,num2))
    
    elif choice==5 :
        print(num1,"%",num2,"=",mod(num1,num2))
        
    else :
        print("invalid choice")
        
"""
area of circle : 2 *3.14 *r 
area of square : 4*slides
area of triangle : 2*(base*height)/2

"""
