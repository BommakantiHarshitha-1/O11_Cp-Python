# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.

import math
def k(n):
    n2 = str(n**2)
    for i in range(len(n2)):
        a, b = int(n2[:i] or 0), int(n2[i:])
        if b and a + b == n:
            return n
			#return (n, (n2[:i], n2[i:]))


def fun_nth_kaprekarnumber(a):
    x1=[]
    x1=[x for x in range(1,100000) if k(x)] 
    return int(x1[a])
    

    

  
    

    