import re

from src.reavnueRec.support.converter import covert_to_number,covert_to_money


class Table:

    def __init__(self, data_frame):
        self.df = data_frame
        self.tableData = []
        self.tableHead = []
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

    def get_list_of_index(self, headersDict):
        desc_table_head = list(self.df[self.tableId].columns.values)
        newList = ((self.df[self.tableId].head(1).values))
        print(type(desc_table_head))
        regex = r"(Unnamed:\s\d)"
        for i in range(len(desc_table_head)):
            print(desc_table_head[i])
            if re.match(regex, desc_table_head[i]):
                print("Match")
                desc_table_head[i] = newList[0][i]
        print(desc_table_head)
        self.tableHead = desc_table_head
        dictOfindex = {}
        for names in desc_table_head:
            if type(names) is str:
                for data in headersDict:
                    if names in headersDict[data]:
                        dictOfindex[data] = desc_table_head.index(names)
        self.doi = dictOfindex
        print(self.doi)
        return self.doi

    def clean_table(self):
        self.cleanTable.append(self.tableHead)
        descTableHead = self.df[self.tableId].head(len(self.df[self.tableId]) - 3).values.tolist()
        print(descTableHead)
        for i in range(len(descTableHead) - 1):
            for n in range(len(descTableHead[0])):
                if descTableHead[i][n] == -1:
                    descTableHead[i][n] = descTableHead[i + 1][n]
                    descTableHead[i + 1][n] = -1
        print(len(descTableHead))
        for data in descTableHead:
            print(data)
        for i in range(4, len(descTableHead) - 1, 7):
            print(i)
            TempList = [descTableHead[i - 3][0] + " " + descTableHead[i-1][0]
                , descTableHead[i][1],descTableHead[i][2],descTableHead[i][4]]
            self.cleanTable.append(TempList)


    def extract_Data(self):
        self.listofitems = []
        print(self.cleanTable)
        for row in self.cleanTable:
            print(row)
            print(self.doi['price'])
            temp = {}
            if (not ((row[self.doi['name']]) in self.cleanTable[0])):
                temp['Name'] = row[self.doi['name']] + ' X ' + str(row[self.doi['qty']])
                temp['StandAlonePrice'] = covert_to_number(row[self.doi['price']-1])
                temp['Recurent'] = False
                temp['whenToPerform'] = 6
                self.listofitems.append(temp)
        print(self.listofitems)
        return self.listofitems

    def getListOfIndex(self, headersDict):
        try:
            descTableHead = self.df[self.tableId].head(len(self.df[self.tableId])).values.tolist()
            for i in range(len(descTableHead) - 1):
                for n in range(len(descTableHead[0])):
                    if descTableHead[i][n] == -1:
                        descTableHead[i][n] = descTableHead[i + 1][n]
                        descTableHead[i + 1][n] = -1
            self.cleanTable.append(descTableHead[0])
            for i in range(2, len(descTableHead) - 1, 3):
                TempList = [descTableHead[i-1][0] + " " + descTableHead[i + 1][0], descTableHead[i][1],
                            descTableHead[i][2], descTableHead[i][3],
                            descTableHead[i][4], descTableHead[i][5], descTableHead[i][6]]
                self.cleanTable.append(TempList)
            for data in self.cleanTable:
                print(data)
            dictOfindex = {}
            for names in descTableHead[0]:
                if type(names) is str:
                    for data in headersDict:
                        if names in headersDict[data]:
                            dictOfindex[data] = descTableHead[0].index(names)
            self.doi = dictOfindex
            print("777777777777777777777777777777")
            print(self.doi)
            print("777777777777777777777777777777")
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
                temp['StandAlonePrice'] = covert_to_money(row[self.doi['price']])
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
