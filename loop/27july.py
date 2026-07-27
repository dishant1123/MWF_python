"""
perfect number : 

6 factors :1,2,3,6 
sum = 1+2+3 = 6    ====> perfect number 

28 factors : 1,2,4,7,14,28 
sum = 1+2+4+7+14 = 28   ====> perfect number 

100 factors : 1,2,4,5,10,20,25,50,100 
sum = 1+2+4+5+10+20+25+50    ====> 117  ===> not  perfect number 
"""

"""
n=int(input("enter the number : "))  #6 
sum =0 
for i in range(1,n):  # 5 ,6 
    if n % i==0:   # 6  % 5 ==0 
        sum =sum +i   # sum = 6
if sum ==n :  # 6 ==6 
    print("perfect number")
else :
    print("not perfect number")
"""

# reverse  a  number : 
"""
user =123    output : 321 
rev =0 
steps : 
1.  r = num % 10   ===>  1 % 10 = 1   r = 1
2.  rev =rev *10 +4 ===> rev =32 *10 +1  ===> 321 
3.  num = num //10  ===>1 //10  ===>0 
"""
# python built in function  : len  min max  sorted sum 

"""
n=int(input("enter the number : "))  # 123
rev =0
length = len(str(n))  # 3

for i in range(length):  #  2  ,3 
    r=n % 10      # r = 1 % 10 =1 
    rev =rev *10 +r  # rev =32 *10 +1 ===> 321
    n = n//10    # n =1 //10 =0 
    
print("reverse number is : ",rev)
"""

# pelindrome : 
"""
input  : 121   ===>reverse number is  : 121 
         111  ===>rev =111 
         141  ===>rev =141

hint : if num ==rev 
"""
"""n=int(input("enter the number : "))  # 121
rev =0
length = len(str(n))  # 3
temp = n  # temp =121  
for i in range(length):  #  2,3
    r=n % 10      #  r =1 %10 =1 
    rev =rev *10 +r  #  rev = 121
    n = n//10    #   n =0 
    
if temp ==rev :  #121 ==121
    print("pelindrome")
else :
    print("not pelindrome")
"""
# twin number  : 
"""
123 : 
each digit sum = 1+2+3 =6 
each  multiply = 1*2*3 = 6 
sum ==mul   ====> twin number 

22 twin number 
"""
# armstrong number :
"""
user =153 
 digit = 3 
 each digit cube : 1*1*1   5*5*5   3*3*3
   sum  :          1 + 125 +27 ===> 153 amg 
   
user =370 
digit =3 
each digit cube :  3*3*3   7*7*7  0*0*0 
sum              :   27   + 343  +  0 =370  amg 

371 :amg 

user =1634 
digit =4 
each  digit :  1*1*1*1   6*6*6*6  3*3*3*3  4*4*4*4
sum            1 + 1296   + 81 +256  ==>1634  amg 

n=1634 
digit =4 
sum =0 
1. r =num % 10  r = 1 % 10 =1  
2. sum =sum + pow(r,digit)  # sum =1634
3. num = num //10  num = 1 //10  =0 
"""

n=int(input("enter the number : "))  # 1634
sum =0 
digits = len(str(n)) 
temp =n   # 1634
for i in range(digits):  # digits =0 ,4
    r = n %10 
    sum =sum +pow(r,digits)  #
    n = n //10 
    
if temp ==sum : 
    print("armstrong number")
else :
    print("not armstrong number")