#progran to  collect input and save in a dictionary
dicti = []
while True:
    k, l = input("Enter your name and age or stop to end: ").split(" ")
    l = int(l)
    if k == "stop":
        break

    dictionary = {k: l}
    dicti.append(dictionary)

print(f"these are the lists {dicti}")


