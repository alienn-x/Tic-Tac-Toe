from random import choice

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def Checker(l1):
    # checking rows
    rowstrt = [0, 3, 6]
    for row in rowstrt:
        if l1[row] == l1[row + 1] == l1[row + 2]:
            print("Someone won")
            return True

    # chekcing columns
    for i in range(3):
        if l1[rowstrt[0] + i] == l1[rowstrt[1] + i] == l1[rowstrt[2] + i]:
            print("Someone won")
            return True

    # checking diagonals
    if l1[0] == l1[4] == l1[8]:
        print("Someone won")
        return True

    elif l1[2] == l1[4] == l1[6]:
        print("Someone won")
        return True

    return False


def printer(l1):
    for i in range(9):
        if i not in [1, 4, 7]:
            print("|", end="")
        print(f" {l1[i]}", end=" ")
        if i not in [1, 4, 7]:
            print("|", end="")
        if i in [2, 5, 8]:
            print()


def computerMove(l1):
    # horizontal
    goldenPairs = {0: 3, 3: 6, 6: 9}

    for key in goldenPairs:
        if (
            l1[key : goldenPairs[key]].count("X") == 2
            and "O" not in l1[key : goldenPairs[key]]
        ):
            for i in l1[key : goldenPairs[key]]:
                if type(i) == int:
                    l1[l1.index(i)] = "O"
                    printer(l1)
                    return
            break

    # vertical

    for strt in range(1, 4):
        verticalList = [l1[strt], l1[strt + 2], l1[strt + 5]]

        if verticalList.count("X") == 2 and "O" not in verticalList:
            for i in verticalList:
                if type(i) == int:
                    l1[verticalList.index(i) * 3] = "O"
                    printer(l1)
                    return
            break

    # diagonal

    diagonals = [[0, 4, 8], [2, 4, 6]]

    for diagonal in diagonals:
        items = [l1[diagonal[i]] for i in range(3)]
        if items.count("X") == 2 and "O" not in items:
            for i in items:
                if type(i) == int:
                    l1[l1.index(i)] = "O"
                    printer(l1)
                    return
            break
    else:
        options = [x for x in range(len(l1)) if type(l1[x]) != str]
        print('shit')
        try:
            l1[choice(options)] = "O"
        except:
            print("This is a draw")
            return True

        printer(l1)


won, draw = False, False

printer(l1)

while not won and not draw:

    inp = int(input("Choice: "))
    l1[l1.index(inp)] = "X"
    draw = computerMove(l1)
    won = Checker(l1)
