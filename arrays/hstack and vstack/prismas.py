def Prismas(N, M):
    # linhas N colunas M
    formatos = [".|.", "-", "WELCOME"]
    counterLinhas = N
    counterColunas = M
    interacoes = 1
    i = 0

    invert = None
    while counterLinhas > 0:
        if not invert:
            print((M//2-i)*formatos[1] + interacoes *
                  formatos[0] + (M//2-i)*formatos[1])
            counterLinhas -= 1
            interacoes += 2
            i += 3

        if (M//2-i) == 1 and not invert:
            invert = True
            print(
                f'{(M//2-2)*formatos[1]}{formatos[2]}{(M//2-2)*formatos[1]}')
            counterLinhas -= 1
            interacoes -= 2
            i -= 3

        if invert:
            print((M//2-i)*formatos[1] + interacoes *
                  formatos[0] + (M//2-i)*formatos[1])
            # print((M//2+2)*formatos[1])
            i -= 3
            interacoes -= 2
            counterLinhas -= 1


if __name__ == '__main__':
    N = 11
    M = 33
    Prismas(N, M)
