# IsKnightsTour [20 Pts]
# Background:  A "knight's tour in chess is a sequence of 
# legal knight moves such that the knight visits every square 
# exactly once. We can represent a (supposed) knight's tour
#  as an NxN list of the integers from 1 to N2 listing the 
# positions in order that the knight occupied on the tour.  
# If it is a legal knight's tour, then all the numbers from 1
#  to N2 will be included and each move from k to (k+1) will
#  be a legal knight's move. With this in mind, write the 
# function isKnightsTour(board) that takes such a 2d list of 
# integers and returns True if it represents a legal knight's 
# tour and False otherwise. Code for this problem should go in 
# hw5.py and will be autograded!

# To help you undertand how a knight's tour is represented,
# and so you can write your own test cases, here is one example 
# of a successful knight's tour:

# board = [
#           [  1, 60, 39, 34, 31, 18,  9, 64 ],
#           [ 38, 35, 32, 61, 10, 63, 30, 17 ],
#           [ 59,  2, 37, 40, 33, 28, 19,  8 ],
#           [ 36, 49, 42, 27, 62, 11, 16, 29 ],
#           [ 43, 58,  3, 50, 41, 24,  7, 20 ],
#           [ 48, 51, 46, 55, 26, 21, 12, 15 ],
#           [ 57, 44, 53,  4, 23, 14, 25,  6 ],
#           [ 52, 47, 56, 45, 54,  5, 22, 13 ],
#         ]
# assert(isKnightsTour(board)==True)


def isKnightsTour(board):
    # Your code goes here...
    pass

board = [
            [  1, 60, 39, 34, 31, 18,  9, 64 ],
            [ 38, 35, 32, 61, 10, 63, 30, 17 ],
            [ 59,  2, 37, 40, 33, 28, 19,  8 ],
            [ 36, 49, 42, 27, 62, 11, 16, 29 ],
            [ 43, 58,  3, 50, 41, 24,  7, 20 ],
            [ 48, 51, 46, 55, 26, 21, 12, 15 ],
            [ 57, 44, 53,  4, 23, 14, 25,  6 ],
            [ 52, 47, 56, 45, 54,  5, 22, 13 ],
        ]
assert(isKnightsTour(board)==True)

# You can write your own test cases here...
print("All test cases passed....")