# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
    if(len(a)==0):
        return -1
    a.sort()
    l=[]
    dif=0
    
    for i in range(len(a)):
        
        for j in range(i+1,len(a)):
            dif=abs(a[i]-a[j])
            l.append(dif)        
    # your code goes here
    return min(l)
    