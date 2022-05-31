'''
check dominant diagonal
'''



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
def order_matrix1(matrix, b):         # [[2,8,4],[0,4,5],[8,6,2]]
    sun_sbs = 0
    for i in range(len(matrix)):
        sun_sbs = 0
        for j in range(len(matrix)):
            sun_sbs += abs(matrix[i][j])
            if order_matrix():
                matrix = swap_lines_of_matrix(matrix,i,j)
                #להשתמש בפונקציה הםרגקר לבדוק את שאר השורות





def order_matrix(matrix, b):    # [[2,8,4],[0,4,5],[8,6,2]]
    j = 0
    line_swap = 0
    check = 0
    num = 0
    index = 0

    while num != (pow(len(matrix),2) + len(matrix))/ 2:    # num = 3   #  matrix =[[8,6,2],[0,4,5],[2,8,4]]
        while index != len(matrix):
            line = matrix[index]
            abs_list = list(map(abs, line))
            if line[j] >= sum(abs_list) - abs(line[j]):
                matrix = swap_lines_of_matrix(matrix,line_swap,check)    #(matrix,1,2)
                b = swap_lines_of_matrix(b,line_swap,check)
                line_swap += 1                         # 2
            num += 1                                    # 5
            check += 1                                   # 3
            index += 1                                   # 3
        index = len(matrix) - (check-j)                  # 1
        j += 1                                           # 1
        check = index

    return matrix


def swap_lines_of_matrix(matrix,index_line1,index_line2):
    for column in range(len(matrix[0])):
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
    if dominant_pivot(A) == False:
        A = find_max_of_column(A)
        printmat(A)



'''while True:
    choice = input("Choose an option for calculations: \n1.gauss-seidel\n2.jacobi\n")
    if choice == '1':
        print(gauss_seidel(a, b))
        break;
    elif choice == '2':
        print(jacobi(a, b))
        break;
    else:
        print("wrong input try again")'''


def multiply_matrix(mat1, mat2):  # matrixes of n*n
    new_mat = []  # contains the result of the multiplication
    line_index = 0
    vector_col = []
    for line_mat1 in mat1:
        temp_line_mat = []
        for column in range(len(mat2[0])):
            vector_col = []
            for line in range(len(mat1)):
                vector_col.append(mat2[line][column])
            temp_line_mat.append(product_calculation(line_mat1, vector_col))
        new_mat.append(temp_line_mat)
    return new_mat


def product_calculation(vector_line, vector_column):  # Multiply line and column
    result = 0
    for element in range(len(vector_line)):
        result += vector_line[element] * vector_column[element]
    return result


def elementary_matrix(matrix):   # in order to find the invertable matrix
    All_Elementary_matrix = {}
    counter_for_elementary_matrix = 0
    counter_for_elementary_operations1 = (pow(len(matrix), 2) + len(
        matrix)) / 2  # In order to create an upper triangular form for matrix 3 *3 we operate 3+2+1 operations(sum of arithmetic progression)
    while counter_for_elementary_matrix != counter_for_elementary_operations1:
        for column in range(len(matrix)):
            for line in range(len(matrix)):
                if line == column and matrix[line][column] != 0:
                    piv = 1 / matrix[line][column]
                    elementary_mat = create_I_matrix(len(matrix))
                    elementary_mat[line][column] = piv

                    counter_for_elementary_matrix += 1
                    All_Elementary_matrix[
                        counter_for_elementary_matrix] = elementary_mat  # Enter new elementary matrix in the dictionary.

                elif line != column and line > column:
                    elementary_mat = create_I_matrix(len(matrix))
                    piv = - matrix[line][column] / matrix[column][column]
                    elementary_mat[line][column] = piv

                    #result_vector = multiply_matrix(elementary_mat, result_vector)
                    counter_for_elementary_matrix += 1
                    All_Elementary_matrix[counter_for_elementary_matrix] = elementary_mat
    # Until here we receive an upper triangle matrix
    counter_for_elementary_operations2 = ((pow(len(matrix), 2) + len(matrix)) / 2) - len(matrix)
    counter_for_elementary_matrix2 = 0
    while counter_for_elementary_matrix2 != counter_for_elementary_operations2:
        for column in range(len(matrix) - 1, -1, -1):
            for line in range(column - 1, -1, -1):
                if line != column and line < column:
                    elementary_mat = create_I_matrix(len(matrix))
                    piv = - matrix[line][column] / matrix[column][column]
                    elementary_mat[line][column] = piv

                    counter_for_elementary_matrix2 += 1
                    All_Elementary_matrix[
                        counter_for_elementary_matrix + counter_for_elementary_matrix2] = elementary_mat
    mat_i = create_I_matrix(len(matrix))
    mat = create_I_matrix(len(matrix))
    mat_w = create_I_matrix(len(matrix))
    for i in range(len(All_Elementary_matrix) - 1, 0, -1):
        mat_w = All_Elementary_matrix[i]
        mat = multiply_matrix(mat, mat_w)
    return mat


def dominant_pivot(matrix):
    j = 0
    counter = 0
    for i in matrix:
        abs_list = list(map(abs, i))
        if abs(i[j]) >= sum(abs_list) - abs(i[j]):
            counter += 1
        j += 1
    return counter == len(matrix)

def zero_matrix(matrix):
    mat = []
    for i in range(len(matrix)):
        mat.append([0 for i in matrix])
    return mat


MAT = [[-1, -2, 5], [4, -1, 1], [1, 6, 2]]
#b = [[2], [4], [9]]
D = zero_matrix(MAT)
for i in range(len(MAT)):
    D[i][i] = MAT[i][i]
U = zero_matrix(MAT)
L = zero_matrix(MAT)
guess = zero_matrix(MAT)
guess_next = zero_matrix(MAT)
for i in range(len(MAT)):
    for j in range(len(MAT)):
        if i < j:
            U[i][j] = MAT[i][j]
        if j < i:
            L[i][j] = MAT[i][j]
'''invert_D = elementary_matrix(D)
print(elementary_matrix(D))
LU = zero_matrix(MAT)
for i in range(len(MAT)):
    for j in range(len(MAT)):
        LU[i][j] = L[i][j] + U[i][j]
G = multiply_matrix(invert_D, LU)
H = multiply_matrix(invert_D, b)'''



def gauss(matrix,b):

    if dominant_pivot(matrix)==False:
        print("no dominant diagonal-cant do gauss ")
        matrix = order_matrix(matrix, b)
    x = [0 for i in range(len(matrix))]
    temp[0]
    e = 1
    A = []
    for i in range(len(matrix)):
        x[i] = matrix[i][i]
    guess = 0
    while e > 0.000001:
        for k in range(len(matrix)):
            temp = f
            for i in range(len(matrix)):
                x1 = [0 for i in range(len(matrix))]
                f = b[i][0]
                for j in range(len(matrix)):
                    if i != j:
                        f -= matrix[i][j]*x[i][j]
                f /= matrix[i][i]
                x1[k] = f
            A.append(x1)
        print(A)
        e = abs(x1[0]-temp[0])

            #guess = f
        #e = abs(f-guess)
Matrix = [[64,16,4,1],[27,9,3,1],[8,4,2,1],[1,1,1,1]]
b = [[4],[3],[2],[1]]
gauss(Matrix,b)





