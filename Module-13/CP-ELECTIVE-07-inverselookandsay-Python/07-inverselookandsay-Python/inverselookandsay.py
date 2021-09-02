# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

# Prerequisite for the following problem is the above problem.
# Write the function inverseLookAndSay(a) that does the inverse of the above problem, so that, in general:
#       inverseLookAndSay(lookAndSay(a)) == a
# Or, in particular:
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([]) == []
# inverseLookAndSay([(3,1)]) == [1,1,1]
# inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7]
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([(2,3),(1,8),(4,3)]) == [3,3,8,3,3,3,3])

def inverselookandsay(a):
    if(len(a[0])==0):
        return []
    b=[i[0]for i in a]
    c=[i[1]for i in a]
    k=0
    l=[]
    for i in b:
        for j in range(i):
            l.append(c[k])
        k=k+1
    print(l)
    return l
        
            
            
            
        
    

# def inverselookandsay(a):
#     # Your code goes here
#     res=[]
#     for i in a:
#         res=res+[i[1]]*i[0]
#     return res


    
    