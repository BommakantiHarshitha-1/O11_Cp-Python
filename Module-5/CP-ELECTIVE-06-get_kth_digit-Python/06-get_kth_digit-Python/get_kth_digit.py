# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 
#(789,0,9)

def fun_get_kth_digit(digit, k):
    r=abs(digit)//(10**k)
    if (r==0):
        return 0
    else:
        return r%10
    
       
           
	
