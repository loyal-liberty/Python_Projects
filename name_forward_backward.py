# traversing through the string in reverse order

'''
str= input("enter string : ")
a=len(str)
i=0
for j in range(-1,-a-1,-1) :
    print(str[i]," ",str[j])
    i=i+1
'''

str1= input("enter string : ")
str2= str1[::-1]
a= len(str1)
i=0
for j in range(1,a+1):
    print(str1[i]," ",str2[i])
    i=i+1