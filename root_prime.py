# abandoned
# write a shot progranm to check whether the square root of a no. is prime or not


import math

num = int (input("enter a nop. : "))
num = int(math.sqrt(num))
for i in range(2,(num+1)//2):
    if num%i==0:
        print("not prime")
        break
    else:
        print("prime")
        break