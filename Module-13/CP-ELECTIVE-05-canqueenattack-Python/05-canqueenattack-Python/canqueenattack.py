# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine 
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and 
# diagonally.

def canqueenattack(qR, qC, oR, oC):
    if(qR==oR or qC == oC):
        return True
    elif((qR+1==qC) and(oR+1==oC)):
        return True
    return False