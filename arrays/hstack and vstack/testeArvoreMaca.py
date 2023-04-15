import numpy


def frutasNaCasa(s, t, a, b, apples, oranges):
    casa = [i for i in range(s, t+1)]
    arvoreMaca = a
    arvoreLaranja = b
    macasDentro = 0
    laranjasDentro = 0

    for i in apples:
        if s <= i + arvoreMaca <= t:
            macasDentro += 1

    for i in oranges:
        if s <= i + arvoreLaranja <= t:
            laranjasDentro += 1

    print(macasDentro)
    print(laranjasDentro)


if __name__ == '__main__':
    frutasNaCasa(5, 10, 3, 12, [-10, 20, 4], [-30, -50, 40])
