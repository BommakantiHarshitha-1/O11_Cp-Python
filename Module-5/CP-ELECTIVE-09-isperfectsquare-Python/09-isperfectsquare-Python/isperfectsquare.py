# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.
import math
def isperfectsquare(n):
    if n ==("hello"):
        return False
    n=int(n)
    if(n>=0):
        r=math.sqrt(n)
        return (r*r)== float(n)
    else:
        return False
        
    
    

