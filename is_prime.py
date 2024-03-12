# find prime no.

num = int(input("enter a no. : "))
num_mid = int((num/2)+1)
for i in range(2,num_mid):
    rem= num%i
    if rem == 0:
        print("not prime")
        break
else:
    print("prime")
    