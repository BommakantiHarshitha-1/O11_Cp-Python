# nondestructiveRemoveRepeats(L)
# Write the function nondestructiveRemoveRepeats(L), which takes a list L and nondestructively returns a new list in which any repeating elements in L are removed.
# Specify the time complexity based on the solution that you have given.

# Here are the sample test cases.
# For example:
# assert(nondestructiveRemoveRepeats([1, 3, 5, 3, 3, 2, 1, 7, 5]) == [1, 3, 5, 2, 7])
# assert(nondestructiveRemoveRepeats([1, 5, 3, 3, 2, 1, 7, 5]) == [1, 5, 3, 2, 7])
# assert(nondestructiveRemoveRepeats([1, 2, 3, 5, 3, 3, 2, 1, 7, 5]) == [1, 2, 3, 5, 7])

l=[]
def nondestructiveRemoveRepeats(L):
    for i in L:
        if i not in l:
            l.append(i)
            continue
            
    return l
print(nondestructiveRemoveRepeats([1, 2, 3, 5, 3, 3, 2, 1, 7, 5]))

assert(nondestructiveRemoveRepeats([1, 3, 5, 3, 3, 2, 1, 7, 5]) == [1, 3, 5, 2, 7])
assert(nondestructiveRemoveRepeats([1, 5, 3, 3, 2, 1, 7, 5]) == [1, 5, 3, 2, 7])
assert(nondestructiveRemoveRepeats([1, 2, 3, 5, 3, 3, 2, 1, 7, 5]) == [1, 2, 3, 5, 7])
print ("All test cases passed....")