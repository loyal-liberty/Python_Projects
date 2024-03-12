# count and display no. of uppercase, lowercase, vowels and consonants
line = input("enter any line : ")
vowels = consonants = lowercount = uppercount = 0
vowel_list = ["a","e","i","o","u","A","E","I","O","U"]
consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

for i in line:
    if i.islower():
        lowercount += 1

    if i.isupper():
        uppercount +=1
 
    if i in vowel_list:
        vowels+=1
 
    if i in consonant_list:
        consonants+=1
print("number of uppercase letters : ", uppercount)
print("number of lowercase letters : ", lowercount)
print("number of vowels : ", vowels)
print("number of consonants : ", consonants)
    


