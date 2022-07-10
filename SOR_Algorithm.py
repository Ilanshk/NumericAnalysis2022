def pivoting_matrix(matrix):
    for column in range(len(matrix)):
        find_max_of_column(matrix, column)
    printmat(matrix)

def find_max_of_column(matrix,j):
    #element = create_I_matrix(len(matrix))
    #  Find the maximun value in a column in order to change lines
    maxElem = abs(matrix[j][j])
    maxRow = j
    for k in range(j+1, len(matrix)):  # Interacting over the next line,in the same column
        if abs(matrix[k][j]) > maxElem:
            maxElem = abs(matrix[k][j])  # Next line on the diagonal
            maxRow = k
    if maxRow != j:
        swap_lines_of_matrix(matrix, maxRow, j)

def swap_lines_of_matrix(matrix, index_line1, index_line2):
    for column in range(len(matrix[0])):
        temp_value = matrix[index_line2][column]
        matrix[index_line2][column] = matrix[index_line1][column]
        matrix[index_line1][column] = temp_value

def printmat(matrix):
    for i in matrix:
        for j in i:
            print(f'{j}  ')
        print('\n')
    print('\n')


def check_dominant_diagonal(matrix, b):
    # line_indexes_to_swap = []
    index = 0
    for line in matrix:
        if line[index] >= abs(sum(line))-abs(line[index]):
            index += 1
        else:
            sum_values = 0
            #line_index_to_replace_with = 0
            for i in range(index+1, len(line)):
                if line[i] >= abs(sum(line))-abs(line[i]):                 #line_index_to_replace_with = i
                    swap_lines_of_matrix(matrix, index, i)
                    swap_lines_of_matrix(b, index, i)
                    index += 1
    return index == len(matrix)


def sor_method(matrix, b):
    pivoting_matrix(matrix)
    epsilon = 0.000001
    guess = [0 for i in matrix]
    value = 0
    difference = 1
    iterations = 0
    w = 1.1
    if not check_dominant_diagonal(matrix, b):
        print("The matrix you entered has no diagonal matrix,so we will try to check if there will be solution")
        maxIter = 100
        while difference > epsilon and iterations < maxIter:
            for line in range(len(matrix)):
                value = b[line][0]
                for column in range(len(matrix)):
                    if line != column:
                        value -= matrix[line][column]*guess[column]

                value /= matrix[line][line]
                value *= w
                value += (1-w) * guess[line]  #(the value of x in the current iteration)
                difference = abs(guess[line] - value)
                guess[line] = value
            iterations += 1
            print("Iteration number" + str(iterations) + ":")
            print(guess)
        if difference < 0.000001:
            print("Although there was no dominant diagonal,the system of equations converged after"+str(iterations)+"to:")
            print(guess)
        else:
            print("No converge")
    else:
        while difference > epsilon :
            for line in range(len(matrix)):
                value = b[line][0]
                for column in range(len(matrix)):
                    if line != column:
                        value -= matrix[line][column]*guess[column]
                value /= matrix[line][line]
                value *= w
                value += (1 - w) * guess[line]  # (the value of x in the current iteration)
                difference = abs(guess[line] - value)
                guess[line] = value
            iterations += 1
            print("Iteration number" + str(iterations) + ":")
            print(guess)
        print("It took"+str(iterations)+"iterations. The result is:")
        print(guess)


sor_method([[3,-1,1], [-1,3,-1], [1,-1,3]],[[-1], [7], [-7]])