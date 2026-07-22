# ladder if else : 
"""
if con :
    if con :
        print() 
    else :
        print()
elif con :
    if con :
        print()
    else :
        print()
"""

"""
a=int(input("enter the a value : "))
b=int(input("enter the b value : "))
c=int(input("enter the c value : "))

if a>b : 
    if a>c :
        print("a is big")
    else :
        print("c is big")
elif b>a :
    if b>c :
        print("b is big")
    else :
        print("c is big")
else :
    print("same")
"""

# ask user to  enter the character and check it is vowel or consonant or digit or special character or not .
"""
input  : &
ouput  : vowel
"""
"""ch=input("enter the character : ")  # 3

if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
    print("vowel")
elif ch >'a' and ch <='z':  # r > a  and  r <=z 
    print("consonant")
elif ch >'0' and ch <='9':
    print("digit")
else :
    print("special character")

"""

# task :1 ask user to enter the 3 number and  check  big small and medium. 
"""
input a =12 
input b =12
input c =15

output  : c is big a is  medium b is small
"""
a=int(input("enter the a value : "))
b=int(input("enter the b value : "))
c=int(input("enter the c value : "))



if a >= b and a >= c:   # a =12  b=2  c=1 
    big = "a"
    if b >= c:
        medium, small = "b", "c"   # medium ="b"  ,small ="c"
    else:
        medium, small = "c", "b"

elif b >= a and b >= c: # b is biggest
    big = "b"
    if a >= c:
        medium, small = "a", "c"
    else:
        medium, small = "c", "a"

else:                   # c is biggest
    big = "c"
    if a >= b:
        medium, small = "a", "b"
    else:
        medium, small = "b", "a"

print("big number  is  :",big,"medium number is :",medium,"small number is :",small)
# print(a,b,c)
#loop: 
