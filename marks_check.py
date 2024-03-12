total_ques= int(input("Enter total no. of questions : "))
inc_ques= int(input("Enter incorrect no. of questions : "))
unmarked= int(input("Enter unmarked no. of questions : "))

correct=total_ques-inc_ques-unmarked

total_marks = 4*total_ques
marks_obtained = (4*correct)-inc_ques

percentage = (marks_obtained/total_marks)*100

accuracy = (correct/(correct+inc_ques))*100

print(f"marks are {marks_obtained}/{total_marks}")
print(f"percentage = {percentage}%")
print(f"accuracy = {accuracy}")
