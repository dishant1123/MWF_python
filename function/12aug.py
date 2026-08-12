"""
1.employees management system 
2.bank app 
"""

# lambda function : one liner function .

"""
syntax : lambda arg : expression
"""
# ex :1 
"""def add(a,b):
    return a+b
print(add(12,45))

result=lambda a,b : a+b
print(result(12,60))
"""

# ex :2 

"""def big():
    a=int(input("enter a number :"))
    b=int(input("enter another number :"))
    if a>b :
        print("a is big")
    else :
        print("b is big")
big()      

x=lambda a,b : print("a is big")if a>b else print("b is big")
x(12,60)
x(121,60)
x(1,60)

"""

# ex :3 

"""
# y=lambda a,b,c : max(a,b,c)

# y=lambda a : len(a)
y=lambda a : min(a)

print(y((12,60,45)))
print(y([12,60,45]))
print(y({"a":12,"b":60}))
"""

# ex :4 filter : 


"""odd=[] 
even=[]
for i in l1 :
    if i% 2==0:
        even.append(i)
    else :
        odd.append(i)
print(odd)
print(even)

l1=[1,2,3,4,5,6,7,8,9,10]

a=list(filter(lambda x :x % 2 ==0 ,l1))
b=list(filter(lambda x :x % 2 ==1 ,l1))

print(a)
print(b)
"""

"""
task  : 5 take list from user append all element in list and print pelindorme num in list 
 
         input : [121 , 131 , 123 ,145 , 789 ]
         output :  [121,131]
"""
"""l1=[121 , 131 , 123 ,145 , 789 ]
l2=[] 

for i in l1 :
    if str(i) == str(i)[ : :-1] :
        l2.append(int(i))
print(l2)

result =tuple(filter(lambda  x : str(x) ==str(x)[ : : -1] ,l1))
print(result)
"""

# ex :5 map : create new list 

"""l1=[1,6,7,8,9]
l2=[] 

for i in l1:
    result = i*2
    l2.append(result)
print(l2)

result =tuple(map(lambda y : y**2 ,l1))
print(result)

"""

# ex :6 

"""task  : 5 take list from user append all element in list and print pelindorme num in list 
 
         input : [121 , 131 , 123 ,145 , 789 ]
         output :  [121,131,321,541,987]
"""
l1=[121 , 131 , 123 ,145 , 789 ]
l2=[] 
for i in l1: 
    result = str(i) [ : :-1]
    l2.append(int(result))
    
print(l2)

result =tuple(map(lambda x : int(str(x)[ : : -1]) ,l1))
print(result)

# next recusion 