# task :1 ask user to enter the  number and  print the  n natural number sum. 
"""
input  :5 
output  :15     ====> 1+2+3+4+5 =15 

"""
""" 
n=int(input("enter the number : "))  # 
sum =0
for i in range(1,n+1) :  # 5 ,6
    sum =sum +i   # sum =15
print("n natural  number sum is   : ",sum)

"""
# sum  of odd and even number  : 

"""
n=int(input("enter the number : "))  #
evensum=0
oddsum =0 
for i in range(1,n+1):
    if i % 2 ==0:
        evensum +=i
    else :
        oddsum +=i
print("even number sum is : ",evensum)
print("odd number sum is : ",oddsum)
"""

# factorial  : 
"""
5 = 1*2*3*4*5 =120 
6 = 1*2*3*4*5*6 =720
"""
"""n=int(input("enter the number : "))  # 5 
fact=1
for i in range(1,n+1):  # 5 ,6 
    fact=fact*i         # fact =120 
print("factorial is : ",fact)
"""

"""
task  : ask user  to enter the  number and  print  sum and  factorial  both . 
input  : 5 
output  : sum of  n natural number is  : 15 
          factorial of  n natural number is  : 120

"""
# prime number  : 1 ,number itself 
"""
2 factors  : 

4 factors  : 1,2,4  ===> not  prime 
19 factors : 1, 19  ===>  prime 
7 factors  : 1,7 ===> prime  
"""

"""n=int(input("enter the number : "))  # 5 
count =0 

for i in range(1,n+1) :  # 5,6 
    if n % i ==0 :   # 5 % 5  == 0 
        count +=1    # 2  
        
if count ==2 :  #  2==2
    print(n,"is prime number")
else :
    print(n,"is not prime number")
"""
