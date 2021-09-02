# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


# def fun_hasnoprimes(l):
#     for i in range(len(l)):
#         if (len(l)%len(l[i])==0):
#             return False
#         return True

def prime(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True


def fun_hasnoprimes(l):
    # your code goes here
    for i in l:
        for j in i:
            if (prime(j) == True):
                return False
    return True
