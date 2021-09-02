# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.



    # if(len(m1[0])!=len(m2)):return None
    # result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*m2)] for X_row in m1] #zip for multiplicating each element 
    # return result
        

def fun_matrixmultiply(m1, m2):
        # your code goes here
    if(len(m1[0])!=len(m2)): 
        return None
    else:
        m3=[]
        for i in range(len(m1)):
            m3+=[[0]*len(m2[0])]
            
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    m3[i][j]+=m1[i][k]*m2[k][j]
    return m3


    




