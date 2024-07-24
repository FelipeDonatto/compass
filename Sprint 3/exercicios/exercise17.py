def parser(list):
    firstList = []
    secondList = []
    thirdList = []
    evenPieces = len(list) / 3
    
    for i in range(len(list)):
        if i < evenPieces:
            firstList.append(list[i])
        elif i < (evenPieces * 2):
            secondList.append(list[i])
        else:
            thirdList.append(list[i])
    
    print(firstList, secondList, thirdList)
    return firstList, secondList, thirdList



parser([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])