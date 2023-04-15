ids = [1, 2, 3, 4, 5]
EachBirdPoint = []


def QuestionBirds(ListaPontosBird):
    for i in ids:
        EachBirdPoint.append([ListaPontosBird.count(i), i])

    orderedPoints = sorted(EachBirdPoint, key=lambda x: x[0], reverse=True)

# [[3, 3], [3, 4], [2, 1], [2, 2], [1, 5]]
    if orderedPoints[0][0] == orderedPoints[1][0]:
        if orderedPoints[1][0] > orderedPoints[0][0]:
            answer = orderedPoints[0][0]
        else:
            answer = orderedPoints[0][1]
    print(orderedPoints)
    return (answer)


def QuestionBirds_gabriel(ListaPontosBird):

    for id in ids:
        id_values = len(list(filter(lambda x: x == id, ListaPontosBird)))

        if (id_values > max_value):
            max_value = id_values
            max_id = id

        elif (id_values == max_value and max_id > id):
            max_id = id

    return max_id


if __name__ == '__main__':
    passaros = 5
    pontosPassaro = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

    print(QuestionBirds_gabriel(pontosPassaro))
