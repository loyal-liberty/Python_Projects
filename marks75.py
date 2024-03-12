# write a program to create a dictionary with the roll no. name and marks of n students in a class and display the names of students who have marks above 75

n = int(input("how many students : "))
stu={}
for i in range(1,n+1):
    print("enter details of students",(i))
    rollno = int(input("roll no : "))
    name = input("name : ")
    marks=float(input("Marks : "))
    d = {"roll_no": rollno, "name":name, "Marks":marks}
    key = "stu" + str(i)
    stu[key]=d
print("students with marks > 75 are : ")
for i in range(1,n+1):
    key="stu"+str(i)
    if stu[key]["Marks"]>=75:
        print(stu[key])