def mult_matrices(m1, m2):
    if len(m1[0]) != len(m2):
        return 0

    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def print_matriz(m):
    for row in m:
        for elemen in row:
            print(elemen, end=' ')
        print()

matriz_1 = [
    [5, -2, 3],
    [-5, 5, 2],
    [2, -3, 5]
]

matriz_2 = [
    [5, -3, 2],
    [-2, 3, 5],
    [4, 3, 1]
]

print_matriz(mult_matrices(matriz_1, matriz_2))
