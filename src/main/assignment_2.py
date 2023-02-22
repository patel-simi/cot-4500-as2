import numpy as np

def neville_method(x_values,y_values,x):
    #Input the size of the matrix 
    size=3
    matrix= np.zeros((size,size))

    for counter,row in enumerate(matrix):
        row[0]=y_values[counter]
     # the end of the first loop are how many columns you have...
    num_of_points = len(x_values)
    # populate final matrix (this is the iterative version of the recursion 
    #explained in class)
    # the end of the second loop is based on the first loop...
    for i in range(1, num_of_points):
        for j in range(1, i+1):
            first_multiplication = (x - x_values[i]) * matrix[i][j-1]
            second_multiplication = (x - x_values[i-1]) * matrix[i-1][j-1]
            denominator = x_values[i] - x_values[j-1]
            # this is the value that we will find in the matrix
            coefficient = (first_multiplication+second_multiplication)/denominator
            matrix[i][j] = coefficient

    print(matrix[num_of_points-1][num_of_points-1])

def divided_difference_table(x_points, y_points):
    #set up matrix
    size=len(x_points)

    matrix= np.zeros((size,size))

    #fill the matrix
    for index, row in enumerate(matrix):
        row[0] = y_points[index]

    #populate the matrix
    for i in range(1,size):
        for j in range(1,i+1):    
            numerator = y_points[j]-y_points[j-1]
            denominator = x_points[i]-x_points[i-j]

            operation=numerator/denominator
            matrix[i][j]=operation

    print(matrix)
    return matrix
    
    
def get_approximate_result(matrix,x_values,value):
    reoccuring_x_span=1
    reoccuring_px_result=0

    for index in range (1,len(matrix)):
        polynomial_coefficient=matrix[index][index]

        reoccuring_x_span *=(value-x_values[index])

        mult_operation= polynomial_coefficient *reoccuring_x_span

        reoccuring_px_result +=mult_operation

    print (reoccuring_px_result)

def get_x_span(i,j):
    if i==j:
        return i, j-i

    elif j>i:
        return j-i-2,i

    elif i>j:
        return i-j, i

    return None,None

def apply_div_dif(matrix:np.array):
    size=len(matrix)
    for i in range(2,size):
        for j in range(2,i+2):
            #something get left and diagonal left 
            left:float=matrix[i][j-1]
            diagonal_left:float=matrix[i-1][j-1]
            numerator:float=left-diagonal_left

            #something get x_span
            start, end= get_x_span(i,j)

            #something get x's involved 
            list_of_xs_involved = []
            for index in range(start,end):
                list_of_xs_involved.append(matrix[index][0])
            
            unique_xs= set(list_of_xs_involved)
            list_of_uniques = list(unique_xs)

            denominator= list_of_uniques[-1] - list_of_uniques[0]
            #something save into matrix

            operation=numerator/denominator
            matrix[i][j]=operation
    return matrix

def hermite_interpolation(x_values,y_values,slopes):
    x_values= [1.3,1.6,1.9]
    y_values= [0.6200,0.4554,0.2818]

    slopes=[-.0522,-0.5699,-0.5811]
    
    num_of_points =len(x_values)
    matrix=np.zeros((num_of_points*2, num_of_points*2))

    #populate x values
    index=0
    for x in range(0,len(matrix),2):
        matrix[x][0]=x_values[index]
        matrix[x+1][0]=x_values[index]
        index+=1

    #prepopulate with deratives (every other row)
    index=0
    for x in range(1, len(matrix),2):
        matrix[x][2]= slopes[index]
        index+=1

    filled_matrix=apply_div_dif(matrix)
    print(filled_matrix)
    #populate 

if __name__ == "__main__":
    #assuming this is where the points are added and where the code actually runs
    x_values=[3.6,3.8,3.9]
    y_values=[1.675,1.436,1.318]
    approximating_value = 0
    slopes=[-0.0522,-0.5699,-0.581]

    neville_method (x_values,y_values,approximating_value)
    divided_table=divided_difference_table(x_values, y_values)
    approximating_x=7.3
    final_approximation=get_approximate_result(divided_table,x_values,approximating_x)    
    hermite_interpolation(x_values,y_values,slopes)


