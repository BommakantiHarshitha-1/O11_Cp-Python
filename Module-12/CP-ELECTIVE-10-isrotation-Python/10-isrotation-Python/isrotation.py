# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
    x=str(x)
    y=str(y)
    rev=y[::-1]
    if len(x)==len(y):
        res=x[len(x)-2:]+x[0:len(x)-2]
        if (res==y or x==rev) or x==y: return True
        else: return False
    return False
    