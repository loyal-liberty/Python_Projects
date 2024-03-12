fact= int(input("enter number"))
result=1
if fact==0:
    result=1
else:
    while fact>0:
        result = result*fact
        fact=fact-1
print(result)