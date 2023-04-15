def PossibleRate(x1, v1, x2, v2):
    startCanguru1 = x1 + v1
    startCanguru2 = x2 + v2
    menorStart = min([startCanguru1, startCanguru2])
    maiorStart = max([startCanguru1, startCanguru2])
    print(menorStart, maiorStart)
    n = 0
    while (1):
        print(menorStart, maiorStart)
        if (menorStart > maiorStart):
            print("impossivel")
            break
        if (x1 + v1*n == x2 + v2*n):
            print("possivel")
            break
        n += 1


if __name__ == '__main__':
    a = 10
    b = 2

    c = 2
    d = 1
    PossibleRate(a, b, c, d)
