# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
    if (n < 0):
        n = -n;
     
    result = 0; 
    max_count = 1;
    if n<100:
        if n<10:
            return n
        while(n>0):
            a=n
            n=int(n/10 )
        return a
    for d in range(10):
        count = countOccurrences(n, d);
        if (count > max_count):
            max_count = count;
            result = d;
        
         
    return result;

def countOccurrences(x, d):
    count = 0;
   
    while (x):
        if (x % 10 == d):
            count += 1;
        x = int(x / 10);
 
    return count;
         
    
 
     
    