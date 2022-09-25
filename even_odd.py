#Program to determine if an input is even or odd
number = input("Enter number and I will tell you if it is even or odd: \n")
number = int(number)
if number %2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")