# python  data type  : 
"""
1.list      : mutable ===> you can change elements of the  list.
2.tuple     : immutable ===> you can not change elements of the  tuple.
3.set       : mutable ===> you can change elements of the  set. but  only unique elements store in set.
4.dictionary: mutable ===> you can change elements of the  dictionary.
5.string    : immutable ===> you can not change elements of the  string.

"""
# list : mutable  ===>order fix ,  you can change elements of the  list.

"""l1 =[1,2,3,4,"ved" ,True,34+8j,34.5]
print(l1)
print(type(l1))  # <class 'list'>
"""

# list value access though index : 
"""
index start with  0 
"""
"""
l1= [1,2,3,45,67,89,78]

print(l1)
print(l1[3])  # indexnumber 3 
"""
# update list value  : 2 indexnumber value change  ===> mital 
"""
l1[2] ="mital"
print(l1)
"""

# built in function  :  len min max  sorted sum 

"""
l1= [1,22,8,10,12]
print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))  # asc to  desc 
print(sorted(l1,reverse=True))  # desc to  asc
print(sum(l1))
"""

# method : 
l1= [1,22,8,10,12,8]

"""l1.append(234)   # add element to the end of the list
l1.append(234)   # add element to the end of the list
l1.append(34.6)
l1.append("hetvi")
print(l1)
"""
"""l2 =l1.copy()
print("l2 :",l2)
"""

"""l1.clear()  # clear the list
print(l1)
"""

"""l2=['mital','ved','hetvi']
l1.extend(l2)
print(l1)
"""
"""print(l1.index(12))
print(l1.index(8))
"""
l1= [1,22,8,10,12,8]

# print(l1.count(8))

# l1.sort()
# print(l1)

# l1.reverse()
# print(l1)

# pop , remove : 

# l1.pop()  # note : if you don't give arg then pop automatically remove the  last element of the list.
# l1.pop(3)   # note : if you given arg in pop then  pop remove index number wise . 
# print(l1)

# l1.remove(22)  # remove element from the list
# print(l1)


# insert : 
"""l1.insert(4,"hetvi")
print(l1)
"""

# task :1 
"""
input : l1= [1,2,3,4,5,6,7,8,9]
output  : odd =[1,3,5,7,9]
          even =[2,4,6,8]

"""
"""l1= [1,2,3,49,5,6,7,8,97]
odd=[]
even=[]
for i in l1:
    if i % 2==0 :
        even.append(i)
    else :
        odd.append(i)
print("odd elements :",odd)
print("even elements :",even)
"""