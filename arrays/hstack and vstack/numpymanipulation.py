import numpy


def rowmeans():
    n, p = [int(x) for x in input().split()]
    b = []
    for i in range(n):
        a = [float(x) for x in input().split()]
        b.append(a)

    x = numpy.array(b)

    colunas = numpy.around(x.mean(axis=1), decimals=2)
    print(colunas)


if __name__ == '__main__':
    rowmeans()
