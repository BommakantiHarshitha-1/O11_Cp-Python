# recusive binarySearchValues(L, v) [20 pts] [autograded]
# Write the recursive function binarySearchValues(L, v) that takes a sorted list L and a value v and returns a list 
# of tuples, (index, value), of the values that binary search must check to verify whether or not v is in L. As an 
# example, say:
#    L = ['a', 'c', 'f', 'g', 'm', 'q']
#    v = 'c'
# Binary search always searches between some lo and hi index, which initially are 0 and (len(L)-1). So here, lo=0 
# and hi=5. The first index we try, then, is mid=2 (the integer average of lo and hi). The value there is 'f', so we 
# will add (2, 'f') to our result.
# Since 'f' is not the value we are seeking, we continue, only now we are searching from lo=0 to hi=1 (not hi=2 
# because we know that index 2 was too high!).
# Now we try mid=0 (the integer average of lo and hi), and so we add (0, 'a') to our result.
# We see that 'a' is too low, so we continue, only now with lo=1 and hi=1. So we add (1, 'c') to our result. We 
# found 'c', so we're done. And so we see:
#     L = ['a', 'c', 'f', 'g', 'm', 'q']
#     v = 'c'
#     assert(binarySearchValues(L, v) == [(2,'f'), (0,'a'), (1,'c')])
# Hint: Do not slice the list L, but rather adjust the indexes into L. 

# def recursion_binarysearchvalues(L, v):
#     return binarysearch(L,v,0,len(L)-1)
    
# def binarysearch(L,v,low,high,res=[]):
#     mid=(low+high)//2 #0,1
#     if (L[mid] == v and low<high):#acfgmq #a
#         res.append((mid,L[mid]))
#         return res
#     elif(low == high):#1,1
#         res.append((mid,L[mid]))
#         return res
#     elif(v<L[mid]):#a<f
#         high=mid-1 #1 low 0
#         res.append((mid,L[mid]))#mid=0
#     else:
#         low=mid+1
#         res.append((mid,L[mid]))
#     return binarysearch(L,v,low,high,res)

# # L = ['a', 'c', 'f', 'g', 'm', 'q']
# # v = 'z'
# # print(recursion_binarysearchvalues(L,v))
def binary_search2(arr,low,high,x,res):
    	# res = []
	if high >= low:

		mid = (high + low) // 2
		print('midval',mid,'lowval',low,'highval',high)
		if arr[mid] == x:
			temp = (mid, arr[mid])
			print(temp)
			res.append(temp)
			return res
			# return mid

		elif arr[mid] > x:
			temp = (mid, arr[mid])
			print(temp)
			res.append(temp)
			return binary_search2(arr, low, mid - 1, x, res) 
		else:
			temp = (mid, arr[mid])
			print(temp)
			res.append(temp)
			return binary_search2(arr, mid + 1, high, x, res) 
	else:
		return res


def recursion_binarysearchvalues(L, v):
	res =[]
	# Your codes goes here
	arr = L
	low = 0
	high = len(L)-1
	x = v
	return binary_search2(arr,low,high,x,res)
	
