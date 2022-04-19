'''
check dominant diagonal
'''


def dominant_diagonal(A):
    for line in range(len(A)):
        sum_values = 0
        for column in range(len(A)):
            if line != column:
                sum_values += abs(A[line][column])
        if A[line][line] < sum_values:
            return False
    return True


def sum_line_values(matrix,lineIndex):
    sum_line = 0
    for col in range(len(matrix)):
        if col != lineIndex:
            sum_line += matrix[lineIndex][col]
    return sum_line

def find_max_of_column(matrix):
            #element = create_I_matrix(len(matrix))
            #  Find the maximun value in a column in order to change lines
    j =0
    maxElem = abs(matrix[0][0])
    maxRow = 0
    for k in range(1,len(matrix)):  # Interacting over the next line,in the same column
        for t in range(k+1, len(matrix)):
            if (abs(matrix[k][t]) > maxElem):
               maxElem = abs(matrix[k][t])  # Next line on the diagonal
               maxRow = k
               matrix = swap_lines_of_matrix(matrix,maxRow,t)
    return matrix

'''def zero(matrix):
    mat = []
    sum_val = 0
    for i in range(len(matrix)):
        mat.append([0 for i in matrix])
    for line in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[line][column] >=



    return mat'''






def swap_lines_of_matrix(matrix,index_line1,index_line2):
    for column in range(len(matrix)):
        temp_value = matrix[index_line2][column]
        matrix[index_line2][column] = matrix[index_line1][column]
        matrix[index_line1][column] = temp_value
    return matrix


def create_I_matrix(size):
    matrixI =[]
    for i in range(size):
        matrixI_helper = []
        for j in range(size):
            if i == j:
                matrixI_helper.append(1)
            else:
                matrixI_helper.append(0)
                matrixI.append(matrixI_helper)
        return matrixI


def printmat(matrix):
    for i in matrix:
        for j in i:
            print(f'{j}  ')
        print('\n')
    print('\n')

def gauss_seidel(A,b):
    if dominant_diagonal(A) == False:
        A = find_max_of_column(A)
        printmat(A)


A= [[2,10,4],[0,4,5],[4,2,0]]
b= [[6],[2],[5]]

print(gauss_seidel(A,b))