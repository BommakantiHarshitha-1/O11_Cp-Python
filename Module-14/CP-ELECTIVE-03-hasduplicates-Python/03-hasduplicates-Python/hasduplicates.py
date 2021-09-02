# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
    # your code goes here
    a=[]
    for i in L:
        for j in i:
            a.append(j)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if (a[i]==a[j]):
                return True
      
    return False