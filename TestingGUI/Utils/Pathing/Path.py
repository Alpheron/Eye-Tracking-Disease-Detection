import csv


def dataProcessing():
    dataList = []
    with open('/Users/Tinku/Desktop/Eye-Tracking-Disease-Detection/TestingGUI/Utils/Pathing/path.csv', newline='') as csvfile:
        dataReader = csv.reader(csvfile, delimiter=',')
        for row in dataReader:
            rowList = []
            for x in row:
                rowList.append(int(x))
            dataList.append(rowList)
    return dataList
