import pandas
import numpy


def verArray():
    y, x = [int(x) for x in input().split()]
    b = []
    for i in range(y):
        a = [int(x) for x in input().split()]
        b.append(a)

    numbers = numpy.array(b)

    print(numbers)


if __name__ == '__main__':
    verArray()
