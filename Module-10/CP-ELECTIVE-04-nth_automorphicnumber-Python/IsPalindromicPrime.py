def ispalindromeprime(n):
    
    reverse=int(str(n)[::-1])
    if n==reverse:
        count=0
        # if x>1:
        for i in range(1,n+1):
            if(n%i)==0:
                count = count+1
        if count == 2:
            return True
        else:
            return False
    else:
        return False
print(ispalindromeprime(2))