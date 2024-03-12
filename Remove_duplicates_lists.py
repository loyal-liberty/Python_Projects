list=[1,2,3,5,6,9,3,2,4,9,6,3,1,5,5]
set1=set(list)
duplicate=[]
unique=[]
for i in set1:
    a=list.count(i)
    print(f"frequncy of {i} is {a}")
    if a>1:
        duplicate.append(i)
    else:
        unique.append(i)
print(duplicate)
print(unique)
