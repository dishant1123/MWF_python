# slicing  in list  : 
"""
pos : l to  r 
neg : r  to l 
"""


l1= [1, 23,45, 267, 89, 455, 67,  888, 90]
#    0  1  2   3    4    5    6    7   8 
print(l1[0])
print(l1[2: 5])  # 2 index   5 end index 
print(l1[1:4]) 
print(l1 [  : 5])  # by deafult  start index is 0
print(l1 [4 : ])  

print(l1[-1])
print(l1[-6  : -2])
print(l1[ 2 :5 :2])  # start index 2 end index 5  step size :2 
print(l1[ 1 :6 :3])  # start index 1 end index 6  step size :3 
print(l1[  : :2])  
print(l1[  : :-2])  
print(l1[  : :-1])    # list reverse



