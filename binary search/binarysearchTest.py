def binary_search(arr, x):
    pivo = len(arr)//2
    low = 0
    high = len(arr)
    ammount = 0
    while (low <= high-1):

        if (arr[pivo] == x):
            ammount += 1
            if arr[pivo+1] == x:
                direita = pivo
                direita += 1
                ammount += 1
                while arr[direita+1] == x:
                    ammount += 1
                    direita += 1

            if arr[pivo-1] == x:
                esquerda = pivo
                esquerda -= 1
                ammount += 1
                while arr[esquerda-1] == x:
                    ammount += 1
                    esquerda -= 1
            return ammount

        elif (x < arr[pivo]):
            high = pivo - 1
            pivo = (low + high)//2
        else:
            low = pivo+1
            pivo = (low + high)//2

    return ammount


if __name__ == "__main__":
    testArr = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
    print(binary_search(testArr, 5))
