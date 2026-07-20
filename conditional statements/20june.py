"""
conditional statement :

if  else : 
syntax : 

if condition :
    print()
else :
    print()

"""
# ex :1 

"""
age =int(input("enter the age : "))

if age >18 :
    print("eligible for voting")
else :
    print("not eligible for voting")
"""

# ex :2 greater than 

"""
a=int(input("enter the a value : "))
b=int(input("enter the b value : "))

if a>b :
    print("a is  big")
else :
    print("b is big")
"""

# ex :3 odd even
"""
num =int(input("enter the num : "))
if  num % 2 ==0 :   # 4 % 2  ==0 
    print("even")
else :
    print("odd")
"""

# task :1 ask user to enter the  number  and  check it is  divisible  by  5  or not. 

# nested if : 
"""
syntax : 

if condition :
    print()
elif condition :
    print()
else :
    print()
"""

# ex :5 
"""
a=int(input("enter the a value : "))
b=int(input("enter the b value : "))

if a>b :
    print("a is  big")
elif b>a :
    print("b is big")
else :
    print("both number are same")
"""

# ex :6  ask user to enter the 3 number  and check which  one is  big . 

"""a=int(input("enter the a value : "))
b=int(input("enter the b value : "))
c=int(input("enter the c value : "))

# a>b and a>c   b>a b>c  c>a c>B 

if a>b and a>c :
    print("a is big")
elif b>a and b>c :
    print("b is big")
elif c>a and c>b:
    print("c is big")
else :
    print("all number are same")

"""

# ex :7  ask user to enter the number and check it  is  divisible  by  5  or 11  or both or not .
"""
input  : 55   ===> number  is  div by  both  5 and  11 
"""

"""num =int(input("enter the num : "))

if num % 11 ==0 and num % 5 ==0 :
    print("divisible by  5 and 11 both")
elif num % 5==0:
    print("divisible by  5 ")
elif num % 11 ==0 :
    print("divisible by  11")
else :
    print("not divisible by  11 and 5")
    
"""

# grade 

maths =int(input("enter the maths marks : "))
science =int(input("enter the science marks : "))
physics =int(input("enter the physics marks : "))

percent = (maths + science + physics)/3 

"""
percent   grade 

90 +       grade A+ 
80-90      grade A
70-80      grade B+ 
60-70      grade B
50-60      grade C+
40-50      grade C
below 40   Fail 
"""

# ask user to enter the 3 side  and check which triangle is like equilateral , isosceles or scalene .
"""
equilateral  : all side  are equal
isosceles    : two side  are equal
scalene      : no side  are equal
"""

"""
task :1 

ask user to enter the cost price and selling  price and print  profit  or  loss . 
profit  = selling  price - cost  price
loss  = cost  price - selling  price

task :2 ask user to enter the salary  and calculate the  gross salary. 

salary          HRA%      DA% 
<10000            20      10 
<20000            25      15
above 20000       30      20 

hint  : gross salary  = salary + HRA +DA 
        HRA  = salary * HRA   like  : if user enter the  salary 10000 then  HRA is  : 
            10000 * 20 /100 = 2000
        DA  = salary * DA   like  : if user enter the  salary 10000 then  DA is  : 
            10000 * 10/100 = 1000
        gross salary  = salary + HRA + DA =10000 + 2000 +1000 = 13000

"""

