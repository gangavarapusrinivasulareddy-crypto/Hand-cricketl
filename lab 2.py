'''def findSquare(num):
    result = num * num
    return result
square = findSquare(6)
print('Square:', square)
'''
'''import math
square_root = math.sqrt(9)
print("Square Root of 4 is",square_root)
power = pow(4, 5)
print("2 to the power 3 is",power)
'''
'''def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)
add_numbers(2, 3)
add_numbers(a = 2)
add_numbers()
'''

'''def find_sum(*numbers):
    result = 0
    for num in numbers:
        result = result + num  
    print("Sum = ", result)
find_sum(1, 2, 3)
find_sum(4, 9)
'''
'''message = 'hello'
def greet():
    print("local", message)
greet()
print("global", message)
'''

c = 1 
def add():
     global c
    c = c + 2 
    print(c)
add()
