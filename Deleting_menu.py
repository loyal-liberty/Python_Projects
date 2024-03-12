# write a program that displays option for inserting or deleting elements in a list. if the user chooses the deletion option displays a submenu and ask is element to be deleted by its value or position or a list slice is to be deleted

val = [17,23,18,19]
print("the list is : ",val)
while True:
    print("Main menu")
    print("1.Insert")
    print("2.Delete")
    print("3.Exit")
    ch=int(input("enter your choice 1/2/3 : "))
    if ch==1:
        item=int(input("enter item : "))
        pos=int(input("enter at which position? : "))
        index=pos-1
        val.insert(index,item)
        print("success! list now is ",val)
    elif ch==2:
        print("Deletion menu")
        print("1.Delete using value")
        print("2.Delete using index")
        print("3.Delete a sublist")

        dch = int(input("enter choice 1 or 2 or 3 : "))
        if dch==1:
            item=int(input("enter item to be deleted : "))
            val.remove(item)
            print("list is now ", val)

        elif dch==2:
            index=int(input("enter index of item to be deleted : "))
            val.pop(index)
            print("list is now ",val)

        elif dch ==3:
            l=int(input("enter lower limit of slice to be deleted : "))
            h=int(input("enter upper limit of slice to be deleted : "))
            del val[l:h]
            print("list is now ",val)
        else:
            print("valid choices are 1/2/3 only")
    elif ch==3:
        break
    else:
        print("valid choices are 1/2/3 only")
