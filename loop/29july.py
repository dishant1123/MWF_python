# while  loop  : 
"""
syntax : 

i= intial value  (start) 
while con :
    print()
    inc/dec 

"""
# ex :1  print 1=100 
"""i=1              # 1 
while i<=100 :   #  101 <=100 
    print(i,end=" ")  # 1 2 3 100    
    i = i +1        # 101

"""

# ex :100-1 
"""i=100 
while i >=1 :
    print(i,end=" ")
    i=i-1 
"""

# prime  : 
"""n=int(input("enter the number : "))  # 5 
i=1 
count =0 
while i<=n :
    if n % i ==0 :
        count =count +1
    i=i+1
if count ==2 :
    print("prime number")
"""

# HW  : twin , amg , perfect ,rev , pelindrome 

# nested for  loop : 
"""
syntax : 

for i in range(n) :
    for j in range(m) :

"""

# ex: ask user to enter the starting number and  ending number and  print prime number between the two numbers.

"""
start = int(input("enter the starting number : "))  # 15 
end = int(input("enter the ending number : "))  # 100 

for i in range (start,end+1):  # 16 , 101
    count =0            # count =0 
    for j in range(1,i+1):  # 15,16  
        if i % j==0 :       #  if 15 % 15 ==0
            count =count +1 # 4
    if count ==2 : # 4 ==2 
        print(i,end=" ")  # 17 
        
"""

# amg in range : 

"""start = int(input("enter the starting number : "))  # 15 
end = int(input("enter the ending number : "))  # 100 

i=start    # 100   
while i <=end:    # 100 <= 10000
    temp = i      # temp =100 
    sum =0       # sum = 0 
    digits = len(str(i))   # digits =3 
    
    while temp > 0 :  # 100 > 0 
        r = temp %10
        sum = sum + pow(r,digits)
        temp = temp //10
    if sum ==i :    # 
        print(i,end=" ") #  
    i = i +1
"""

#hw : range ===> pelindrome ,perfect 