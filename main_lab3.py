# функция-решатель
def solver_function(t):  # t - масив параметров
    out = open('output.txt', 'w')

    # случай 5 (все пары)
    if t[0] == t[1] == t[2] == t[3] == t[4] == t[5] == 0:
        out.write('5')

    # случай 0 (нет решений)
    elif (t[0] == t[1] == 0 and t[4] != 0) or (t[2] == t[3] == 0 and t[5] != 0):
        out.write('0')

    # случай 0  (нет решений)
    elif t[0] != 0 and t[5] - (t[4] * t[2] / t[0]) != 0 and t[3] - (t[1] * t[2] / t[0]) == 0:
        out.write('0')

    # случай 0  (нет решений)
    elif t[1] != 0 and t[5] - (t[4] * t[3] / t[1]) != 0 and t[2] - (t[0] * t[3] / t[1]) == 0:
        out.write('0')

        # случай 1 (cистема имеет бесконечно много решений, которые имеют вид y = kx+n)
    elif (t[0] != 0 and t[1] != 0 and t[3] - (t[1] * t[2] / t[0]) == 0 and t[5] - (
            t[4] * t[2] / t[0]) == 0):
        s = -1 * (t[0] / t[1])
        n = t[4] / t[1]
        out.write(f'1 {s} {n}')

        # случай 1 (cистема имеет бесконечно много решений, которые имеют вид y = kx+n)
    elif (t[2] != 0 and t[3] != 0 and t[1] - (t[3] * t[0] / t[2]) == 0 and t[4] - (
            t[5] * t[0] / t[2]) == 0):
        s = -1 * (t[2] / t[3])
        n = t[5] / t[3]
        out.write(f'1 {s} {n}')

        #  случай 2 (система имеет единственное решение)
    elif (t[0] * t[3] - t[1] * t[2]) != 0:
        d = t[0] * t[3] - t[1] * t[2]
        d1 = t[4] * t[3] - t[1] * t[5]
        d2 = t[0] * t[5] - t[4] * t[2]
        out.write(f'2 {d1 / d} {d2 / d}')


    # случай 3 (x = x0, y0 - любое)
    elif t[1] == t[3] == 0:
        if t[0] != 0:
            x = t[4] / t[0]
        else:
            x = t[5] / t[2]
        out.write(f'3 {x}')

    #  случай 4 (y = y0, x0 - любое)
    elif t[0] == t[2] == 0:
        if t[1] != 0:
            y = t[4] / t[1]
        else:
            y = t[5] / t[3]
        out.write(f'4 {y}')

    out.close()
    return out



file=open('input.txt') # читаю входные данные и складываю в масив
abcdpq=[float(i) for i in file.readline().split()]
file.close()
solver_function(abcdpq) # вызываю фуекцию-решатель












