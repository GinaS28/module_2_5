def get_matrix (n, m, value):
    matrix = []
    for i in range (n):
        matrix.append([])
        for j in range (m):
            matrix[i].append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print('1)', result1)
print('2)', result2)
print('3)', result3)
