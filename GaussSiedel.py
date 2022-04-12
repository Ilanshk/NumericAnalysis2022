'''
check dominant diagonal
'''


def dominant_diagonal(A):
    flag = -1
    for line in range(len(A)):
        sum_values = 0
        for column in range(len(A)):
            flag = 0
            if line != column:
                sum_values += abs(A[line][column])
        if A[line][line] >= sum_values:
            flag = 1
    if flag == 1:
        return True
    else:
        return False

