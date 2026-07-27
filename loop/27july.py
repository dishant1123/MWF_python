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

"""n=int(input("enter the number : "))  # 123
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
# armstrong number :

# nested loop   + pattern  : 