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
            if (i== cnt):
                elem[i]= 1
            else:
                elem[i]= 0
        cnt+=1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
# take first row and multiply corresponding values with next column
def matrix_mult( m1, m2 ):

    for elem1 in m1: #first row of the first matrix or Counter of the current row examined, thus current column
        for i in range(len(elem1)):#cycle through the row getting the necessary index
            for elem2 in m2: #take relevant column
                elem2[i]= elem2[i]*elem1[i]




# function setting up matrix
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

'''
test section
'''
'''
test1= [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
test2= new_matrix()

print_matrix(test1)
print("~~~~~~~~~~~~")
print_matrix(test2)

ident(test1)
print_matrix(test1)

ident(test2)
print_matrix(test2)
'''
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
matrix_mult(A,B)
print(A)
print(B)
matrix_mult(B,A)
print(A)
print(B)
matrix_mult(ident(A),A)
print(A)
