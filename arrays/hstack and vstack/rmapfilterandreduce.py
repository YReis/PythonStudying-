def vezes3(array):

    resposta = list(map(lambda x: x*3, array))
    print(resposta)


def potencia(array):
    indices = list(range(len(array)))
    resposta = list(map(lambda x, y: x**y, array, indices))
    print(resposta)


def contains(arr1, arr2):

    resposta = list(filter(lambda x: x in arr2, arr1))
    print(resposta)


def mapProva(nomes):
    def nomesCompostos(x):
        y = x.split(' ')
        return f'{y[0][0].upper()}.{y[1][0].upper()}.'

    resposta = list(map(nomesCompostos, nomes))
    print(resposta)


if __name__ == '__main__':
    arrayb = [2, 6, 5, 7, 2, 9]
    arr = [3, 4, 5, 6, 7, 8]
    nomes = ["jose henrique", "maria antonia", "joao pedro", "bento couto"]
    vezes3(arr)
    potencia(arr)
    contains(arr, arrayb)
    mapProva(nomes)
