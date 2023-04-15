k = 3


def binary_search(arr, x):

    distinctSortedArr = list(set(sorted(arr)))

    distinctSortedArrSearch = []
    for i in distinctSortedArr:
        distinctSortedArrSearch.append(i-3)

    for i in distinctSortedArrSearch:

        pivo = len(distinctSortedArr)//2
        low = 0
        high = len(distinctSortedArr)
        while (low <= high-1):

            if (arr[pivo] == i):
                print([i, i+3])
                break

            elif (i < distinctSortedArr[pivo]):

                high = pivo - 1
                pivo = (low + high)//2
            else:
                low = pivo + 1
                pivo = (low + high)//2


if __name__ == "__main__":
    testArr = [1, 5, 2, 2, 2, 5, 5, 4]

    binary_search(testArr, 3)
