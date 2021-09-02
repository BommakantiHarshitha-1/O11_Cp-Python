# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
    n=abs(n)
    pd=-1
    while(n>0):
        od=n%10
        if od == pd:
            return True
        pd=od
        n=n//10
    return False
        
        
        