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

def reverse_list(l1):
    l2=[]

    for i in l1 :   # 123
        result =str(i)[ : : -1]  # result = "321" 
        l2.append(int(result))   # l2.append(121)
    return l2
print(reverse_list([121,123,456,89]))
