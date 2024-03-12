# write a program to input the value of x and n and print the sum of series
# 1+x+x^2+x^3+...x^n

x = int(input("enter value of x : "))
n = int(input("enter the power(n) : "))
sum = 0
for i in range(n+1):
    term = x**i
    sum = sum + term

print(sum)
