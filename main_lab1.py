file1 = open('input.txt')
input = [i.strip() for i in file1.readlines()]  # переписываю значения из входного файла, для удобного использования
file1.close()
degree = int(input[0])  # натуральное число - степень полинома
x = int(input[-1])  #  аргумент p(x)
output = open('output.txt', 'w')

if degree != 0:
    odds = input[1].split()  # коэффициенты полинома p(x)
    sum = int(odds[0]) * x  # первое слогаемое схемы горнера


    for i in range(degree - 1):
        sum = x * (sum + int(odds[i + 1]))  # цикл для схемы


    output.write(str(sum + int(odds[-1])))  # добавляем свободный член полинома
else:
    output.write(input[1])
output.close()