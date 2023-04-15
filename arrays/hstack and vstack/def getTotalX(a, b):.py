def getTotalX(a, b):
    resposta = []
    allpossibles = [int(i) for i in range(a[0], b[-1] + 1)]

    for number in allpossibles:
        divisible = True
        divisor = True
        for div in b:
            if number % div != 0:
                divisible = False
                break
        for div in a:
            if div % number != 0:
                divisor = False
                break
        if divisible and divisor:
            resposta.append(number)
    return len(resposta)
