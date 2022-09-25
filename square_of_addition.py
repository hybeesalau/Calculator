first_number = int(input('Enter first number:\n'))
second_number = int(input('Enter second number:\n'))

def add(a, b):
    return a + b

def square (c):
    return c * c

result = square(add(first_number,second_number))
print('Result is',result)
