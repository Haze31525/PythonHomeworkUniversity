def CaseOfStartOfGame(leftMis, leftKan, rightMis, rightKan):
    def visualization():
        print(leftMis, leftKan - 2, rightMis, rightKan + 2)
        print(leftMis, leftKan - 1, rightMis, rightKan + 1)
        print(leftMis, leftKan - 3, rightMis, rightKan + 3)
        print(leftMis, leftKan - 2, rightMis, rightKan + 2)
        print(leftMis - 2, leftKan - 2, rightMis + 2, rightKan + 2)
        print(leftMis - 1, leftKan - 1, rightMis + 1, rightKan + 1)
        print(leftMis - 3, leftKan - 1, rightMis + 3, rightKan + 1)
        print(leftMis - 3, leftKan, rightMis + 3, rightKan)
        print(leftMis - 3, leftKan - 2, rightMis + 3, rightKan + 2)
        print(leftMis - 3, leftKan - 1, rightMis + 3, rightKan + 1)
        print(leftMis - 3, leftKan - 3, rightMis + 3, rightKan + 3)

    if leftMis < 3 or leftKan < 3:
        return CaseOfEndOfGame(leftMis, leftKan, rightMis, rightKan)

    visualization()
    leftMis -= 3
    leftKan -= 3
    rightMis += 3
    rightKan += 3

    return CaseOfStartOfGame(leftMis, leftKan, rightMis, rightKan)


def CaseOfEndOfGame(leftMis, leftKan, rightMis, rightKan):
    if leftMis == 0 and leftKan == 0:
        return "Задача решена!"

    if leftMis == leftKan: # -> leftMis == 1 and leftKan == 1
        rightKan -= 1
        rightMis -= 1
        leftMis += 1
        leftKan += 1
        print(leftMis, leftKan, rightMis, rightKan)

        rightMis += 2
        leftMis -= 2
        print(leftMis, leftKan, rightMis, rightKan)

        rightKan -= 1
        leftKan += 1
        print(leftMis, leftKan, rightMis, rightKan)

        leftKan -= 2
        rightKan += 2

    elif leftKan != 0:
        rightKan -= 1
        leftKan += 1
        print(leftMis, leftKan, rightMis, rightKan)

        leftKan -= 2
        rightKan += 2
    else:
        rightKan -= 1
        leftKan += 1
        print(leftMis, leftKan, rightMis, rightKan)

        leftKan -= 1
        rightKan += 1
        leftMis -= 1
        rightMis += 1
    print(leftMis, leftKan, rightMis, rightKan)

    return CaseOfEndOfGame(leftMis, leftKan, rightMis, rightKan)


def game(leftMis, leftKan):
    if leftMis >= leftKan and (leftKan % 3 != 2 or leftMis % 3 != 2):
        return CaseOfStartOfGame(leftMis, leftKan, 0, 0)
    return "Задача не может быть решена"


print(game(int(input("Введите кол-во миссионеров: ")), int(input("Введите кол-во каннибала: "))))
