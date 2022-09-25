w = int(input('Enter Weight:\n'))
h = int(input('Enter Height:\n'))

def bmi(x, y):
    bmi1 = x / (y * y)
    return bmi1

result = bmi(w,h)
print('Body Mass index is',result)


