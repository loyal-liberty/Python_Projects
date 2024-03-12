num = int(input("enter a no. greater than 20 : "))
for i in range(11,num):
    if i%3==0 and i%7==0:
        print("tipsytopsy")
    if i %3==0:
        print("tipsy")
    elif i%7==0:
        print("topsy")
    else:
        print(i)