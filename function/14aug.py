# *arg : number of argument

# ex :1 
"""
def add(*arg) :
    return sum(arg)
print(add(12,34,56,78,90,1,2,3,4,5))
"""

# ex :2 

"""def n_sum(*x):
    sum =0 
    for i in x :
        sum+=i
    return sum 
print(n_sum(1,2,3,4,5,6,7,8,9,10))
print(n_sum(1,2,3,4,5))
print(n_sum(11.45,2))
"""

# **kwarg :used in dict 

"""def dict_student(**kwarg) :
    for  i ,j  in kwarg.items() : # items ---> dict method print  both key and value
        print(f"{i} : {j}")

dict_student(name="mital",age=20,gender="female")
dict_student(name="hetvi",age=21)
"""
# recusion  function  : function call itself

# ex :1 

"""
5!    :  n * (n-1)!  =====> 5 * (5-1)!  ====> 5 *4!  ====>120  
"""

"""def facto(n):
    if n==1:
        return 1
    else :
        return n * facto(n-1)
print(facto(5))
print(facto(6))
"""

# ex :2 

"""
5  ====> 5 + (n-1)
"""
"""def n_sum(n):
    if n==0 :
        return 0
    else :
        return n + n_sum(n-1)
    
print(n_sum(5))
"""

# fibonacci seris  : 

"""n=int(input("enter number :"))
a,b=0,1  # =====> a=0 b=1 

for i in range(n):  # n=3,5 
    print(a)   # 0 1 1 2
    c=a+b      # c = 3 
    a=b        # a=2 
    b=c        # b=3
"""

# using recusion  # 0 1 1 2 3 5 8 

"""def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return fibo(n-1) + fibo(n-2) 
n=10
for i in range(n):
    print(fibo(i))
"""

# employees management system  : dict 

"""
1.add
2.delete
3.update
4.search
5.display 

"""
d1={}
def add():
    id= int(input("enter id :"))
    name=input("enter name :")
    salary=int(input("enter salary :"))
    d1[id] =[name,salary]
    
def delete_emp():
    id =int(input("enter id  you want to delete :"))
    if id in d1 :
        del d1[id]
    else :
        print("id not found")

def update():
    id =int(input("enter id  you want to update :"))
    if id in d1 :
        name =input("enter  new name :")
        salary =int(input("enter new salary :"))
        d1[id][0]=name
        d1[id][1]=salary
    else :
        print("id not found")

def search():
    id =int(input("enter id  you want to search :"))
    if id in d1 :
            print(d1[id])
            
    else :
            print("id not found")
        
add()
add()
print(d1) 
# delete_emp()

# print(d1)

# update()

# print(d1)

search()
print(d1)
"""
id    name  salary  
101    mital   20000
102    hetvi   30000

"""
