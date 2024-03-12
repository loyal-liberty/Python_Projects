# for first n terms

first = 0
second = 1
n = int(input("enter no. of terms : "))
print(first,second,end=" ")
for i in range(n-2):
    term = first+second
    first = second
    second = term
    print(term,end=" ")
