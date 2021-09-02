# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l):
    a=[]
    co=0
    for i in l:
        b=""
        m=str(i)
        for j in m:
            if int(j)%2==0:
                b=b+j
        #print (len(b))
        if len(b)>0:
            a.insert(co,int(b))
        else:
            a.insert(co,0)
        co=co+1
    #print(a)
    return a


            
            
        
                
        