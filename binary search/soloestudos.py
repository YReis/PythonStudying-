def binary_search(arr, x):
    pivo = len(arr)//2
    low = 0
    high = len(arr)
    while (low <= high-1):
        print(pivo, low, high)
        if (arr[pivo] == x):
            return x
        elif (x < arr[pivo]):
            high = pivo - 1
            pivo = (low + high)//2
        else:
            low = pivo+1
            pivo = (low + high)//2
    return "nao esta na lista"


if __name__ == '__main__':
    array = [2, 3, 4, 5, 6, 7, 8]
    x = 5

    print(binary_search(array, x))
