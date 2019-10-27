def isInPolygon(xPoint, yPoint, xPolygon, yPolygon):
    result = 0
    for i in range(len(xPolygon)):
        if (((yPolygon[i] <= yPoint < yPolygon[i - 1]) or (yPolygon[i - 1] <= yPoint < yPolygon[i]))
                and (xPoint > (xPolygon[i - 1] - xPolygon[i]) * (yPoint - yPolygon[i]) / (
                        yPolygon[i - 1] - yPolygon[i]) + xPolygon[i])):
            result = 1 - result
    return result



def main(fileName):
    resultAnswer = []
    xPolygon = []
    yPolygon = []
    xTestingPoint = []
    yTestingPoint = []
    amountOfPolygonPoints = 0
    amountOfTestingPoints = 0
    count = 0
    with open(fileName) as f:
        amountOfPolygonPoints = int(f.readline());
        for line in f:
            if (count == amountOfPolygonPoints):
                amountOfTestingPoints = int(line)
            elif (count < amountOfPolygonPoints):
                x, y = line.split()
                xPolygon.append(float(x))
                yPolygon.append(float(y))
            elif (count > amountOfPolygonPoints):
                x, y = line.split()
                xTestingPoint.append(float(x))
                yTestingPoint.append(float(y))
            count = count + 1

    for i in range(0, len(xTestingPoint)):
        print("point: ", xTestingPoint[i], " ", yTestingPoint[i])
        isInP = isInPolygon(xTestingPoint[i], yTestingPoint[i], xPolygon, yPolygon)
        if (isInP == 1):
            resultAnswer.append(True)
            print("result: true")
        if (isInP == 0):
            resultAnswer.append(False)
            print("result: false")
    return resultAnswer
main("file.txt")
