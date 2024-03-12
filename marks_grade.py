# a tuple stores marks of a students in 5 subjects. Write a program to calculate the grade of the students.

marks=eval(input("enter marks tuple : "))
total = sum(marks)
avg = total/5

if avg>=75:
    grade = "A"
elif avg>=60:
    grade = "B"
elif avg>=50:
    grade = "C"
else:
    grade = "D"
print(f"total marks : {total}, grade : {grade}")