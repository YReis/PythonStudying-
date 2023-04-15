def binary_search(arr, x):
    pivo = len(arr)//2
    low = 0
    high = len(arr)
    while (low <= high-1):
        print("again")
        if (arr[pivo] == x):
            anterior = pivo

            while arr[anterior-1] == x:
                anterior -= 1
            return anterior

        elif (x < arr[pivo]):
            high = pivo - 1
            pivo = (low + high)//2
        else:
            low = pivo+1
            pivo = (low + high)//2
    return "nao encontrado"


if __name__ == "__main__":
    testArr = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]

    print(binary_search(testArr, 2))
