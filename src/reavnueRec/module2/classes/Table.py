from src.reavnueRec.support.converter import covert_to_number


class Table:

    def __init__(self, data_frame):
        self.df = data_frame
        self.tableData = []
        self.listofitems = []
        self.cleanTable = []

    def getTable(self, headersList):
        headersList = [element.lower() for element in headersList]
        tableHeads = []
        scoreHeaders = []
        for i in range(len(self.df)):
            tableHeads.append(self.df[i].head(1).values)
        for data in tableHeads:
            scoreHeaders.append(0)
            for i in range(len(data)):
                if type(data[0][i]) is str:
                    if data[0][i].lower() in headersList:
                        scoreHeaders[-1] += 1
        self.tableId = scoreHeaders.index(max(scoreHeaders))
        return self.tableId

    def getListOfIndex(self, headersDict):
        try:
            descTableHead = self.df[self.tableId].head(11).values.tolist()
            for i in range(len(descTableHead) - 1):
                for n in range(len(descTableHead[0])):
                    if descTableHead[i][n] == -1:
                        descTableHead[i][n] = descTableHead[i + 1][n]
                        descTableHead[i + 1][n] = -1
            self.cleanTable.append(descTableHead[0])
            for i in range(1, len(descTableHead) - 1, 3):
                TempList = [descTableHead[i][0] + " " + descTableHead[i + 2][0], descTableHead[i + 1][1],
                            descTableHead[i + 1][2], descTableHead[i + 1][3],
                            descTableHead[i + 1][4], descTableHead[i + 1][5], descTableHead[i + 1][6]]
                self.cleanTable.append(TempList)
            dictOfindex = {}
            for names in descTableHead[0]:
                if type(names) is str:
                    for data in headersDict:
                        if names in headersDict[data]:
                            dictOfindex[data] = descTableHead[0].index(names)
            self.doi = dictOfindex
            return self.doi
        except (AttributeError, NameError, IndexError, TypeError):
            print("Error Occurred")

    def extractData(self):
        self.listofitems = []
        print(self.cleanTable)
        for row in self.cleanTable:
            temp = {}
            if (not ((row[self.doi['name']]) in self.cleanTable[0])):
                temp['Name'] = row[self.doi['name']] + ' X ' + str(row[self.doi['qty']])
                temp['Price'] = covert_to_number(row[self.doi['price']])
                temp['Recurent'] = False
                temp['whenToPerform'] = 0
                self.listofitems.append(temp)
        print(self.listofitems)
        return self.listofitems

# t1 = Table('/home/vimukthi/Desktop/sale2.pdf')
#
# print(t1.getTable(['SALESPERSON', 'P.O.', 'SHIP DATE', 'SHIP VIA', 'F.O.B.', 'TERMS']))
#
# print(t1.getTable(['item no:', 'item no', 'item #', 'item code:', 'item code', 'no', '#', 'description', 'desc'
#                       , 'details', 'detail', 'qty', 'quantity', 'unit price', 'total', 'amount', 'number', 'sum'
#                       , 'volume', 'aggregate']))
# print(t1.getListOfIndex(headersDict))
#
# print(t1.extractData())
