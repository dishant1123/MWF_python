"""
python  : 
1. high programming languges 
2. object oriented programming
3. interpreted programming languages 

use : 
1.backend : ===> framework django ,flask ,odoo 
2.data analysis :   ===> insights  ===> numpy ,pandas ,matplotlib ,seaborn
3.data cleaning : ===> 
4.AI -ML : machine learning ,artificial intelligence
5.GUI : graphical user interface
6.game development :
7. hacking 
extention : .py 

run  : VS code ,jpyter ,annaconda ,google colab

project : spootify , you tube , PUBG ,
"""

# print("hello world")
"""print("my name is ved")
print("my name is ram")

print("shah")
"""
# comment: 
"""
1.single line comment  : # 
2.multi line comment   :  ''' '''  or """ """ 
"""
# escap sequence character :

"""
1.\n : new line
2.\t : tab
3.\b : backspace
4. end =  : end of line   ===> remove white space
"""

# print("ram\n")
# print("shah")
# print("ramt\t\t shah")

# print("ram\b\bshah")

"""print("dishant",end="\b\b")
print("shah")
"""
# variable declaration  rules : 
"""
1. any variable you can't start with digit , special character 
    exception : _  ====> valid for variable 

2. you can end variable digit 

"""

# data type  : 
"""
1.int  : pos  or neg 
2.float  : decimal 
3.char/string : a to z ,digits ,
4.bool  : True,False 
5.complex  : 1. real part  , 2.immiginary part  
"""

"""a=9023452345345345634563453456456456   # a variable , 90 static value 
print(a)
print(type(a))
print("a=",a)

b=23556.45456564565676767
print(b)
print(type(b))
print("b=",b)

c= "abnm"
print(c)
print(type(c))

d=True
print(d)
print(type(d))

e = 23 + 8j 
print(e)
print(type(e))
f= 45+20j 
print(f+e)
"""

# convert data type 

"""a=90 
print(a)
print("a is  int : ",type(a))
print("a value  convert in to float : ",float(a))
print("a value  convert in to complex : ",complex(a))
print("a value  convert in to string : ",str(a))
print("a value  convert in to bool : ",bool(a))
"""

# user input  int  : 

"""
a=int(input("enter the  a  number :"))
b=int(input("enter the  b  number :"))

print("a=",a)
print("b=",b) # note : int data type  not store float value.  
"""

# user input  float  :

"""a= float(input("enter the  a  number :"))
b= float(input("enter the  a  number :"))

print("a=",a)
print("b=",b) # note : float data type  store int value.  
"""

# string user input :

"""a=str(input("enter the  a  name :"))
b= input("enter the  b  sur-name :")

print(a)
print(b)
print(type(a))
"""

# ask user to enter the two int data type number and  concate them.
"""
input a =10 
input b =20
output 1020
"""

# operator  : 
"""
1. airthmetic operator : + - * / % //
2. relational operator : == != > < >= <=
3. logical operator : and  not
4. assignment operator : = += -= *= /= //= %=
5. membership operator : not in ,in
"""

# print(20 % 10)   # remainder  
# print(10/3)
# print(10//3)

# a=1 
# b=10
# print(a!=b)
# print(a>b and a!=b)
# print(a>b or a!=b)
# a =a +b    # a+=b 
# a+=b
# print(a)

# l1 =[1,2,3,4,5]
# print(2 in l1)
# print(2 not in l1)

# conditional statement :

"""
if con : 
    print()
else :
    print()
"""

# ex :1 
"""age =int(input("enter the  age :"))

if age >18 :
    print("eligible  for vote")
else :
    print("not eligible  for vote")
"""

# ex :2 odd or even 

"""num =int(input("enter the  number :"))

if num % 2 ==0:
    print("even")
else :
    print("odd")
""" 

# ex :3  nested if : 
"""
a=int(input("enter the  a  number :"))
b=int(input("enter the  b  number :"))

if a>b :
    print("a is big")
elif b>a :
    print("b is big")
else :
    print("same")
    
"""
# ex :4 
"""a=int(input("enter the  a  number :"))
b=int(input("enter the  b  number :"))
c=int(input("enter the  c  number :"))

if a>b and a>c :
    print("a is big")

elif b>a and b>c :
    print("b is big")
    
elif c>a and c>b :
    print("c is big")

else :
    print("same")
"""

# ex :5 

phy=int(input("enter the  phy  marks :"))
che=int(input("enter the  che  marks :"))
maths=int(input("enter the  maths  marks :"))

total = phy + che + maths
print("total marks :",total)
percent = (total)/3
print("percent :",percent)

"""
percent     Grade 
above 90    A+ 
80-90       A
70-80       B+
60-70       B
50-60       C+
40-50       C
below 40    Fail 
"""

