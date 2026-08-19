# iterator : 

ex :1 
"""
sales =[10000,25000,45000,17000,35000]

s = iter(sales)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
"""

# ex :2 

"""
sales =[10000,25000,45000,17000,35000]

try :
    total_sales = iter(sales)
    print(next(total_sales))
    print(next(total_sales))
    print(next(total_sales))
    print(next(total_sales))
    print(next(total_sales))
    print(next(total_sales))
    
except StopIteration :
    print("no more sales")
"""

# ex :3 enumerate :

'''sales =[10000,25000,45000,17000,35000]

"""
day 1 -> 10000
day 2 -> 25000
day 3 -> 45000
day 4 -> 17000
day 5 -> 35000
"""

for days , amt in enumerate(sales,1) :
    print(f"days {days} -> {amt}")
    
'''
# ex :4 zip : 

"""sales =[10000,25000,45000,17000,35000]
products =['keyboard','monitor','printer','projector','speakers']


for i ,j in zip(sales,products):
    print(f"sales : {i} , product : {j}")

for days,( i ,j) in enumerate(zip(sales,products),1) :
    print(f"days {days} -> sales : {i} , product : {j}")
"""

# ex :5 generator :
"""
def sales_generator(sales):
    for i in sales :
        yield i

sales =[10000,25000,45000,17000,35000]

s=sales_generator(sales)
print("days 1 -> 10000")
print("days 2 -> 25000")
"""
def sales():
    yield 10000
    yield 25000
    yield 45000
    yield 17000
    yield 35000

s=sales()
print("days 1 -> 10000")
print("days 2 -> 25000")
print("days 3 -> 45000")
print("days 4 -> 17000")
print("days 5 -> 35000")