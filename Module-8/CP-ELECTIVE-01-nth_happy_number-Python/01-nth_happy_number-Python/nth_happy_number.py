# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)


def Happynum(n):
    sum = 0
    while(n!=0):
        sum += (n%10)**2
        n//=10
    if sum == 1:
        return True
    elif sum<10:
        return False
    else:
        return Happynum(sum)
def nth_happy_number(n):
    f = 1
    g = 0
    while(f<=abs(n)):
        g+=1
        if(Happynum(g)):
            f+=1
    return g
