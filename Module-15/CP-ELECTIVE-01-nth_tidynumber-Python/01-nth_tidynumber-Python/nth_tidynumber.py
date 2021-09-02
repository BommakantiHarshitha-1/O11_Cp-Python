# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def  tidy(num):
    pr=10
    c=num
    while(num):
        rm=num%10
        num//=10
        if rm >pr:
            return False
        pr=rm
    return True
def fun_nth_tidynumber(n):
    f=0
    g=0
    while f<=n:
        g=g+1
        if(tidy(g)):
            f=f+1
    return g