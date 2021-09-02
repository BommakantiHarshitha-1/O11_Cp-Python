# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def isprime(x):
    count=0
    if x>1:
        for i in range(1,x+1):
            if(x%i)==0:
                count = count+1
        if count == 2:
            return True
        else:
            return False
  
#helper function to find the squares of digits
def numSquareSum(n):
    squareSum = 0;
    while(n>0):
        squareSum += (n % 10) * (n % 10);
        n = int(n / 10);
    return squareSum

# method return true if
# n is Happy number
def ishappynumber(n):
    # initialize slow
    # and fast by n
    slow = n;
    fast = n;
    while(True):

        # move slow number
        # by one iteration
        slow = numSquareSum(slow);
        # move fast number
        # by two iteration
        fast = numSquareSum(numSquareSum(fast));
        if(slow != fast):
            continue;
        else:
            break;

    # if both number meet at 1,
    # then return true
    if (slow == 1):
        return True
    else:
        return False

#finding nth happy primes

def fun_nth_happy_prime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        
        if ((ishappynumber(guess)) and (isprime(guess))):
            found += 1
            
    return guess