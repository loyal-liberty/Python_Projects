# write a program to input the value of x and n and print the sum of series

# x+(x^2/2!)-(x^3/3!)+...(-1)^n(x^n/n!)

x = int(input("enter value of x : "))
n = int(input("enter the power(n) : "))

sum = x
sign = 1

for i in range(2,n+1):

    fact = 1

    for j in range(1,1+i):
        fact= fact*i
    
    term = (sign*(x**i))/fact
    sum = sum + term
    sign = sign * (-1)

print(sum)
