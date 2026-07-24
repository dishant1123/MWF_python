"""
loop : iteration   ====> repeation   

1. for loop  :
2. while loop  :
3. while True loop 
"""
"""
for  loop  : 

syntax : 

for variable name in range(start ,stop ,step ) :
    print(variable name)
"""

# ex :1-100 
"""
for i in range(0,101):  # 101 ,101 
    print(i,end=" ")  # 1 2 3 100   
    
"""
# 100-1 : 
"""
for x in range(100,0,-1):
print(x,end=" ")
"""

# odd : 
"""
for i in range(1,101,2):  # 101 ,101 
    print(i,end=" ")  # 1 2 3 100   
"""
# even :  1-100 
"""
for i in range(2,101,2):  # 101 ,101 
    print(i,end=" ")  # 1 2 3 100   
"""

# -10  to +10   :-10 -9 -8 .... 0  1 2 3 ...9 
"""
for i in range(-10,10):  #-10,10   
    print(i,end=" ")  #    
"""

# 10 to -10    # 10 9 8 7   0 -1 -2 -3   -9 
"""for i in range(10,-10,-1):  #   
    print(i,end=" ")  #    
"""


# tasks : 
"""
1. print  a to  z  like a,b,c,d .....z 
2. print -90 to  90  like  -90 -87  -84 ... 
3. print 90 to  -90  like  90 87  84 ... 0   
4. Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".

Sample Output :
fizzbuzz
1
2
fizz
4
buzz 


5.Write a python program to count total number of notes in given amount.
hint : 50 100 200 500 
input  : 650 
output  : 500 rs 1 note 
          100 rs 1 note 
          50 rs 1 note


"""

# solution 3 :

"""for i in range(1,21) :
    if i % 3 == 0 and i % 5 == 0 :
        print(i,"fizzbuzz")
    elif i % 3 == 0 :
        print(i,"fizz")
    elif i % 5 == 0 :
        print(i,"buzz")
"""
# solution 4 :
"""amount =int(input("enter amount : "))  # 750 

note500 =0 
note100 =0
note50  =0

if amount >=500 :  # 750 >=500 
    note500 = amount // 500   # note500  = 750 // 500 =1 
    amount -= note500 * 500   # amount =amount -note500 *500  = 250 
    
if amount >=100 :  # 250 >= 100 
    note100 = amount // 100   # note100 = 250 //100 = 2 
    amount -= note100 * 100   # amount  =250-200 =50  

if amount >=50 :  # 50 >=50 
    note50 = amount // 50  
    amount -= note50 * 50
    
print("500 notes : ",note500)
print("100 notes : ",note100)
print("50 notes : ",note50)
"""