# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


        
def isrotated(str1, str2):  
    if len(str1) != len(str2):
        return False 
    str3 = str1 + str1 
    if (str3.count(str2)> 0):
        return True
    else:
        return False
    

 
