num = int(input())
o_num=num
reverse=0

while num>0:
    digit=num%10
    num=num//10
    reverse=reverse*10 + digit

print(o_num,reverse)