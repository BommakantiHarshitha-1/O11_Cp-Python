# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
    count=0
    l=[] 
    while (hand>0): # 123> 0 , 12 >0
        a=int(hand%10) #12.3 a = 3 , 12%10 = 1.2 a= 2
        hand=int(hand/10) #123 = 123/10 = 12, 12/10 =1
        l.insert(count,a) # 0th place a=3
        count=count+1
    l.reverse()
    return tuple(l)
