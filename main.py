from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 40, 0, 100 ]

#draws a square given bottom left starting point and size
def drawSquare(screen,color,x,y,size):
    matrix = new_matrix(2,2)
    add_edge(matrix,x,y,0,x+size,y,0)
    add_edge(matrix,x+size,y,0,x+size,y+size,0)
    add_edge(matrix,x+size,y+size,0,x,y+size,0)
    add_edge(matrix,x,y+size,0,x,y,0)
    draw_lines(matrix, screen, color)

x0=0
y0=0
for i in range(70):
    drawSquare(screen,color,x0,y0,100)
    x0+=10
    y0+=10
    color[0]+=10
    color[1]+=5

x0=0
y0=500
for i in range(70):
    drawSquare(screen,color,x0,y0,100)
    x0+=10
    y0-=10
    color[0]-=10
    color[1]+=20

'''
test section 
'''

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]

matrix_mult(A,B)
print("~~~~~~~~~Multiplying A*B~~~~~~~~~~")
print("printing A")
print_matrix(A)
print("printing B")
print_matrix(B)
print("~~~~~~~~~Multiplying B*A (b has been altered)~~~~~~~~~~")
matrix_mult(B,A) #note B has been altered
print("printing A")
print_matrix(A)
print("printing B")
print_matrix(B)

print("~~~~~~~~~More Cases~~~~~~~~~~")
Z = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
C = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
ident(Z)
matrix_mult(Z,C)
print("testing ident")
print("printing C")
print(C)
print("printing Z (z*c where z is identity)")
print(Z)

display(screen)
