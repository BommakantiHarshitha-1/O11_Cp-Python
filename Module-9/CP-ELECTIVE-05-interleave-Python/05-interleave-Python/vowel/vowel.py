def vowel(n):
    count=0
    for i in range(len(n)):
        if(n[i]=="a" or n[i]=="e" or n[i]=="i" or n[i]=="o" or n[i]=="u"):
            count=count+1
    return count

n=input("enter a string")
print(vowel(n))