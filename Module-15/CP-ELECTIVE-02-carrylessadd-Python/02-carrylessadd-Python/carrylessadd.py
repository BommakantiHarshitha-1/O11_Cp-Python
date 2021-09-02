 # carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
    res=0
    a=1
    b=0
    while(x or y):
        b=((x%10)+(y%10))
        b=b%10
        res=(b*a)+res
        x=x//10
        y=y//10
        a=a*10
    return res
  

