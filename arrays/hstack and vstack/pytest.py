def funcSum(n, k, ar):
    validos = []
    setOfArr = ar
    tamanhoDoSet = len(setOfArr)

    while setOfArr:
        compare = setOfArr[0]
        setOfArr.pop(0)
        for x in setOfArr:
            if (compare + x) % k == 0:
                validos.append([compare, x])

    return len(validos)


if __name__ == '__main__':
    print(funcSum(5, 3, [1, 3, 2, 6, 1, 2]))
