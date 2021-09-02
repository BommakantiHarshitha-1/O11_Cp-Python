def prime(n):
    count=0
    if n>1:
        for i in range(1,n+1):
            if(n%i)==0:
                count +=1
        if count==2:
            return True
        else:
            return False

def sum(n):
    sum=0
    while n>0:
        digi=n%10
        digi=sum+digi
        n=n//10
    return sum

def addictive(n):
    if (not prime(n)):
        return False
    else:
        return True
print(addictive(29))