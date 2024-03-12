num=int(input("enter no."))
str=str(num)
num_len = len(str)

print("number is ",num)
print("first digit is ",str[0])
print("last digit is ",str[-1])

f_digit=(int(str[0]))**num_len
l_digit=(int(str[-1]))**num_len

print(f_digit,l_digit)

