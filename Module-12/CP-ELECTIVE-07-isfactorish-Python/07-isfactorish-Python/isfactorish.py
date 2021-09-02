# Write the function fun_isfactorish(n) that takes a value int n, 
# and returns True if n is a (possibly-negative) integer with exactly 3 unique digits 
# (so no two digits are the same), where each of the digits is a factor of the number 
# n itself. In all other cases, the function returns False (without crashing).
# For example:
#  assert(fun_isfactorish(412) == True) # 4, 1, and 2 are all factors of 412
#  assert(fun_isfactorish(-412) == True) # Must work for negative numbers!
#  assert(fun_isfactorish(4128) == False) # 4128 has more than 3 digits
#  assert(fun_isfactorish(112) == False) # 112 has duplicate digits (two 1's)
#  assert(fun_isfactorish(420) == False) # 420 has a 0 (0 is not a factor)
#  assert(fun_isfactorish(42) == False) # 42 has a leading 0 (only 2 unique digits)

def noofDigits(n):
    c = 0
    while(n > 0):
        n = n//10
        c = c+1
    return c
def fun_isfactorish(n):
    n=abs(n)
    s=str(n)
    if len(s)>3:
        return False
    if(noofDigits(n) != 3 ):
        return False
    else:
        d1 = n % 10
        n = n // 10
        d2 = n % 10
        n = n // 10
        d3 = n % 10

        if(d1 == 0 or d2 == 0 and d3 == 0):
            return False

        if(d1 == d2 or d2 == d3 or d3 == d1):
            return(False)

        if (n%d1 == 0 and n%d2 == 0 or n%d3 == 0):
            
            return True
    
    
        
    

