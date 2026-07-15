# print("dishant shah")

"""print('gaurav')
print("ram") 
print("sita")
"""
# comment  : 
"""
1. single  line comment: #
2. multiline  comment  : """ """ or '''  ''' 
"""

# escap-sequence character : 
"""
1. \n : new line  
2. \t : tab
3. \b : backspace
4. end = remove the  white  space
"""
"""
print("\nmy name is dishant shah.\t study in NFSU.")
print("live  in ahm")

print("my name is gaurav sharma\b\b\b live in ahm")
"""

# take a  two  print  statement  and print full name  with space  like  : dishant shah 
"""print("dishant",end=" ")
print("shah")
print("dishant","shah")  # comma create space in python. 
print("my name is dishant shah","live in ahm")
"""

# variable declaration  rules : 
"""
1. variable name  not  start with number , special character. 
    ex : @a=90 , 12a =90  both are not allowed.
2. variable  name  start with  letter  and  can  contain  letter , number , _ .
    ex : a=90 , _ =90 ,a_ =89 , _a=90 are allowed.
3. variable  contain  letter with number  but  number in last like . 
    ex: a12 =90 , b_123 =67 , a_1_2 =90 are allowed.
"""

# data type : 
"""
1. int  : pos or neg 
2. float : decimal value 
3. str / char : a to z , string  , digit , special character
4. bool : True or False
5. complex number :  i or j
    ex :23 +8j   ====> 2 part  : 1.immaginary  part  : 8j  real  part : 23

"""

a =905656575777777557575   # a variable name  90 static value 
print(a)
print("a value is :",a)
print(type(a)) 

b=456789.456789 
print(b)
print("b=",b)
print(type(b))

c="dishant"
print(c)
print("c=",c)
print(type(c))

d =True
print(d)
print("d=",d)
print(type(d))

e=23 +8j
h=34 +9j
 
print(e)
print("e=",e)
print(type(e))
print(e+h)