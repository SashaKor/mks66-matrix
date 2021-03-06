'''
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
'''
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    result=""
    for elem in matrix:
        for i in range(len(elem)):
            if (i != 0 and i % (len(elem)-1) == 0):
                result+= str(elem[i])+"\n"
            else:
                result+= str(elem[i])+" "
    print(result)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
#just loop through and make everything 1 consequently down
def ident( matrix ):
    cnt = 0
    for elem in matrix:
        #looping through the square matrix
        for i in range(len(elem)):
            if (i == cnt):
                elem[i]= 1
            else:
                elem[i]= 0
        cnt+=1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
# take first row and multiply corresponding values with next column
def matrix_mult( m1, m2 ):
    #creates the matrix
    m2_result=[]
    for row in m1: #take each row
        new_row=[]
        for i in range (len(m2[0])): #track columns in second matrix
            cnt=0
            sum=0
            for elem in row: #multiplies row elem with corresponding col elem
                mult_val= elem*(m2[cnt][i])
                sum+= mult_val #calculating all the sums
                cnt+=1
            new_row.append(sum)
        m2_result.append(new_row)

    #reassigns matrix m2
    # directly manipulates second matrix
    m2.clear
    for elem in m2_result:
        #print(str(elem))
        m2.append(elem)


# function setting up matrix
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
