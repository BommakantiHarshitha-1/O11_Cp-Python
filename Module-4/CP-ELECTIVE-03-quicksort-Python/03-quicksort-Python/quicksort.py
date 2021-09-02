"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    # Your code goes here
    if (len(array) < 2):
        return array
    else:
        first = array[0]  
        rest = array[1:]
        
        low = [x for x in rest if x < first]
        high = [x for x in rest if x >= first]
    quick =quicksort(low) + [first] + quicksort(high)
    return quick