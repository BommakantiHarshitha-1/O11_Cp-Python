# rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2)
# A rectangle can be described by its left, top, width, and height. This function 
# takes two rectangles described this way, and returns True if the rectangles 
# overlap at all (even if just at a point), and False otherwise. 
# Note: here we will represent coordinates the way they are usually represented in 
# computer graphics, where (0,0) is at the left-top corner of the screen, and while 
# the x-coordinate goes up while you head right, the y-coordinate goes up while you 
# head down (so we say that "up is down")
def fun_rectangle_overlap(left1, top1, width1, height1, left2, top2, width2, height2):
    factor1=((left2>left1)and(left2>left1+width1))
    factor2=((left1>left2)and(left1>left2+width2))
    factor3=((top2>top1)and(top2>top1+height1))
    factor4=((top1>top2)and(top1>top2+height2))
    if(factor1 or factor2 or factor3 or factor4):
        return False
    else:
        return True

        