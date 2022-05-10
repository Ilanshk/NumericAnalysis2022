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


def printmat(matrix):
    for i in matrix:
        for j in i:
            print(f'{j}  ')
        print('\n')
    print('\n')


def swap_lines_of_matrix(matrix, index_line1, index_line2):
    for column in range(len(matrix[0])):
        temp_value = matrix[index_line2][column]
        matrix[index_line2][column] = matrix[index_line1][column]
        matrix[index_line1][column] = temp_value

# print(check_dominant_diagonal([[15, 5, 8], [2, 10, 4],[14, 1, 1]], [[4], [5], [7]]))



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


def pivoting_matrix(matrix):
    for column in range(len(matrix)):
        find_max_of_column(matrix, column)
    printmat(matrix)


#print("####pivoting####")
#pivoting_matrix([[18, 14, 5], [10, 12, 2], [5, 15, 7]])


def gauss_seidel_method(matrix, b):
    pivoting_matrix(matrix)
    epsilon = 0.000001
    guess = [0 for i in matrix]
    value = 0
    difference = 1
    iterations = 0
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
                difference = abs(guess[line] - value)
                guess[line] = value
            iterations += 1
            print("Iteration number" + str(iterations) + ":")
            print(guess)
        print("It took"+str(iterations)+"iterations. The result is:")
        print(guess)


#gauss_seidel_method([[4,2,0],[2,10,4],[0,4,5]],[[2],[6],[5]])


def jacobi_method(matrix, b):
    pivoting_matrix(matrix)
    epsilon = 0.000001
    guess = [0 for i in matrix]
    temp = [0 for j in matrix]
    value = 0
    difference = 1
    iterations = 0
    if not check_dominant_diagonal(matrix, b):
        print("The matrix you entered has no diagonal matrix,so we will try to check if there will be solution")
        maxIter = 100
        while difference > epsilon and iterations < maxIter:
            for line in range(len(matrix)):
                value = b[line][0]
                for i in range(len(guess)):
                    guess[i] = temp[i]
                for column in range(len(matrix)):
                    if line != column:
                        value -= matrix[line][column] * guess[column]
                value /= matrix[line][line]
                difference = abs(guess[line] - value)
                temp[line] = value
            iterations += 1
            print("Iteration number" + str(iterations) + ":")
            print(guess)
            for i in range(len(guess)):
                guess[i] = temp[i]
        if difference < epsilon:
            print("Although there was no dominant diagonal,the system of equations converged after" + str(
                iterations) + "to:")
            print(guess)
        else:
            print("No converge")
    else:
        while difference > epsilon:
            for line in range(len(matrix)):
                value = b[line][0]
                for column in range(len(matrix)):
                    if line != column:
                        value -= matrix[line][column] * guess[column]
                value /= matrix[line][line]
                difference = abs(guess[line] - value)
                temp[line] = value
            iterations += 1
            print("Iteration number" + str(iterations) + ":")
            print(temp)
            for i in range(len(guess)):
                guess[i] = temp[i]
        print("It took  " + str(iterations) + " iterations. The result is:")
        print(guess)


#print("Jacobi:")
#jacobi_method([[4, 2, 0], [2, 10, 4], [0, 4, 5]], [[2], [6], [5]])


def solve_linear_equation_system():
    matrix = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    b = [[2], [6], [5]]
    print("Choose the method of solving")
    print("1.Jacobi method")
    print("2.Gauss-Seidel method")
    choice = int(input("Enter 1 or 2"))
    if choice == 1:
        jacobi_method(matrix,b)
    elif choice == 2:
        gauss_seidel_method(matrix,b)


solve_linear_equation_system()