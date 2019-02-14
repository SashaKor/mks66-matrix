        """
        A matrix will be an N sized list of 4 element lists.
        Each individual list will represent an [x, y, z, 1] point.
        For multiplication purposes, consider the lists like so:
        x0  x1      xn
        y0  y1      yn
        z0  z1  ... zn
        1  1        1
        """
        import math

        #print the matrix such that it looks like
        #the template in the top comment
        def print_matrix( matrix ):
            result=""
            for elem in matrix:
                for i in range(len(elem)):
                    if (i % len(elem) == 0):
                        result+= str(elem[i])+"\n"
                    else:
                        result+= str(elem[i])
            print(result)

        #turn the paramter matrix into an identity matrix
        #you may assume matrix is square
        #just loop through and make everything 1 consequently down
        def ident( matrix ):
            cnt = 0
            print ("length of this matrix: "+str(n))
            for elem in matrix:
                #looping through the square matrix
                for i in range(len(elem[0])):
                    if (i==cnt):
                        elem[i]= 1
                    else:
                        elem[i]= 0
                cnt++

        #multiply m1 by m2, modifying m2 to be the product
        #m1 * m2 -> m2
        def matrix_mult( m1, m2 ):
            pass



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
        test1= [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
        test2= new_matrix()

        print_matrix(test1)
        print("~~~~~~~~~~~~")
        print_matrix(test2)
