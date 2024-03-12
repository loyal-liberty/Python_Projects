# write a program to find lowest and second lowest from 10 numbers input

small = smaller = 0
for i in range(10):
    num = int(input("enter your number : "))
    if i==0:                # for first number
        small=num

    elif i==1:              # for second number
        if num<small:
            smaller=num
        else:
            smaller=small
            small = num

    else:                   # for third number and onwards
        if num<smaller:
            small=smaller
            smaller=num
        elif num<small:
            small=num

print(smaller,small)