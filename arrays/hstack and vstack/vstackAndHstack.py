import numpy


def diagonalDifference(arr):
    totaldiagonal1 = 0
    totaldiagonal2 = 0
    i = 0

    while i < len(arr):
        digonal1 = arr[i][i]
        totaldiagonal1 += digonal1
        print(totaldiagonal1)
        diagonal2 = arr[i][len(arr)-i-1]
        totaldiagonal2 += diagonal2
        print(totaldiagonal2)
        i += 1


if __name__ == '__main__':
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    diagonalDifference(arr)
