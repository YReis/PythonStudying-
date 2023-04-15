

# encontrar todos os numeros que sejam divididos por todos da primeira
# e divisor de todos da segunda

def allNumbers(divisores, b):

    resposta = []
    allpossibles = [int(i) for i in range(a[0], b[-1] + 1)]
    print(allpossibles)

    for number in allpossibles:
        divisible = True
        divisor = True
        for div in a:
            if number % div != 0:
                divisor = False
                break
        for div in b:
            if div % number != 0:
                divisible = False
                break
        if divisible and divisor:
            resposta.append(number)

    return len(resposta)


if __name__ == '__main__':
    a = [2, 6]
    b = [24, 36]

    allNumbers(a, b)
