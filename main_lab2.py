def matrix_addition(Q, W):
    add = [[0.0] * len(Q[0]) for i in Q]
    for i in range(len(Q)):
        for j in range(len(Q[0])):
            add[i][j] = float(Q[i][j]) + float(W[i][j])
    return add                       # Cложение матриц


def multiplication(Q, a):
    mult = [[0.0] * len(Q[0]) for i in Q]
    for i in range(len(Q)):
        for j in range(len(Q[0])):
            mult[i][j] = a * float(Q[i][j])
    return mult                     # Умножение матрицы на а


def matrix_multiplication(Q, W):
    matr_mult = [[0.0] * len(W[0]) for i in Q]
    for i in range(len(Q)):
        for j in range(len(W[0])):
            for k in range(len(Q[0])):
                matr_mult[i][j] += float(Q[i][k]) * float(W[k][j])
    return matr_mult                     # Умножение матриц


def transposition(Q):
    transp = [['0'] * len(Q) for i in Q[0]]
    for i in range(len(Q[0])):
        for j in range(len(Q)):
            transp[i][j] = Q[j][i]
    return transp               # Транспонирование матрицы



with open('input.txt') as input:
    input = [row.strip().split() for row in input]
    if input[2][0] == input[4][1] and input[2][1] == input[4][0] and input[0][1] == input[2][0]:
        flag = True       # Убеждаюсь в том что, матрицы В и C_transp совпадают по размеру и что можно будет умножить А
    else:
        flag = False

    A = []
    for i in range(0, len(input[1]), int(input[0][1])):  # Матрицы А
        A.append(input[1][i:i + int(input[0][1])])
    B = []
    for i in range(0, len(input[3]), int(input[2][1])):  # Матрицы В
        B.append(input[3][i:i + int(input[2][1])])
    C = []
    for i in range(0, len(input[5]), int(input[4][1])):  # Матрицы C
        C.append(input[5][i:i + int(input[4][1])])

    a = float(input[6][0])

if flag == True:

    C_transp = transposition(C)
    B_a = multiplication(B, a)
    R = matrix_addition(C_transp, B_a)
    X = matrix_multiplication(A, R)

    Xout = ''
    for i in range(len(X)):
        for j in range(len(X[0])):
             Xout += str(X[i][j]) + ' '

    out = open('output.txt', 'w')
    out.write(f'1\n{len(X)} {len(X[0])}\n{Xout}')
    out.close()


else:
    out = open('output.txt', 'w')
    out.write('0')
    out.close()


