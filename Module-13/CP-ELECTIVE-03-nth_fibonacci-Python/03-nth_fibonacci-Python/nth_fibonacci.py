# Background: The Fibonacci numbers are defined by F(n) = F(n-1) + F(n-2). 
# There are different conventions on whether 0 is a Fibonacci number, 
# and whether counting starts at n=0 or at n=1. Here, we will assume that 
# 0 is not a Fibonacci number, and that counting starts at n=0, 
# so F(0)=F(1)=1, and F(2)=2. With this in mind, write the function 
# nthfibonaccinumber(n) that takes a non-negative int n and returns the nth Fibonacci number.



def fun_nthfibonaccinumber(n):
    n1 = 1
    n2 = 1
    if n == 0:
        return n2
    else:
        for i in range(0,n-1):
            sum = n1 + n2
            n1 = n2
            n2 = sum
    return n2