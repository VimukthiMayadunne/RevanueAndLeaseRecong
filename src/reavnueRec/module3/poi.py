import numpy as np
import tabula

from src.reavnueRec.module2.classes.Table import Table
from src.reavnueRec.support.table_data import header_list, headersDict

file_path = "/home/vimukthi/Desktop/p3.pdf"

dfs = tabula.read_pdf(file_path, stream=True, multiple_tables=True, pages='all')


def getpoi(df, extracted_data):
    table = Table(df)
    print(table.getTable(header_list))
    table.df[table.tableId] = table.df[table.tableId].replace(np.nan, -1)
    newList = list(df[0].head(1).values)
    print (newList)
    table.get_list_of_index(headersDict)
    table.clean_table()
    data = table.extract_Data()
    extracted_data['numberOfPerformanceObligations'] = len(data)
    extracted_data['poi'] = data
    return extracted_data


