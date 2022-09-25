students_data = {}
userinput = input("Enter name and age of students or 0 to exit :  ")
stop = "0"
while userinput !=stop:
    student_name, student_age =userinput.split(" ")    #    or write this line  =>   userdata = userinput.split(" ")
    students_data[student_name] = student_age          # or write this                   => val[userdata[0]] = int(userdata[1])
    userinput = input("Enter name and age of students or 0 to exit :  ")
print(students_data)