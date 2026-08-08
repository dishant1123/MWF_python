"""
l1=[1,2,2,3,3,3,4,4,4,5,5,6,6,7,7]
l2=[] 
count =0 
for i in l1 :   # 2
    if i  in l1 :   # if 2 not in l2 
        count +=1
print(l2)

s1="mississippi"
output  : {'m':1,'i' :4 ,'s' :4,'p':2}

for i in s1 :
    if i in s1 :
        d1[i] += 1
    else :
        d1[i] = 1
"""
"""
d1={"phy" :90 , "maths" :91 }
key=input("enter the key :")

if key in d1 :
    print("key found",d1[key])
    print("value   : ",d1[key])
else :
    print("key not found")
"""

# function  type  : 
"""
1. no arg  no return 
2. no arg  with return 
3. with arg  no return
4. with arg  with return
"""

"""
syntax : 

def function_name() :
    print() 
call_function_name()
"""
# 1. no arg  no return 
"""def func():
    print("ved,mital,hetvi")
    
func() 
print("hello")
func() 
print("how are you ??")
func() 
func() 
print("fine")
func() 
"""

# 2. with arg no return 

"""def add(a,b):
    c=a+b 
    print("sum of  the two number is  : ",c)

add(12,45)  # int 
add(12.30,45.60)  # float 
add("mital","patil")  # string
add(True,False)  # boolean
add(12+80j , 13+20j)
add(12,23,45)
"""

# duplicate remove  from the list  : 

# ex :1 no arg no return 
"""
def duplicate_remove() :
    l1 =[1,2,2,3,3,4,4,5,5,6,6,7,8,10]
    l2=[]
    for i in l1 :
        if i not in l2 :
            l2.append(i)
    print(l2)
duplicate_remove()
"""
#ex :2 with arg no return
"""
def duplicate_remove(x) :
    l2=[]
    for i in x :
        if i not in l2 :
            l2.append(i)
    print(l2)

duplicate_remove([1,2,2,3,3,4,4,5,5,6,6,7,8,10])
"""

# ex :3 pelidrome a list : 
"""
def pelidrome() :
    l1=['hetvi','ved','mital','sumit','maam','php']
    l2=[]

    for i in l1 :   # hetvi
        if i == i[ : : -1] :   #if hetvi == hetvi
            l2.append(i)
    print(l2)
pelidrome()
pelidrome()
"""

# ex :4 with arg  no return 

"""
def pelidrome(l1) :
    l2=[]

    for i in l1 :   # hetvi
        if i == i[ : : -1] :   #if hetvi == hetvi
            l2.append(i)
    print(l2)
pelidrome(['hetvi','ved','mital','sumit','maam','php'])
pelidrome(['1221',"aba",'mom','bhai','ben'])
"""

# reverse list : l1 =[121,123,456,89] using function  

l1 =[121,123,456,89] 
l2=[]

for i in l1 :   # 123
    result =str(i)[ : : -1]  # result = "321" 
    l2.append(int(result))   # l2.append(121)
print(l2)

