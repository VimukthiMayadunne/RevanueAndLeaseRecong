import numpy as np

from src.reavnueRec.module2.classes.Table import Table
from src.reavnueRec.support.table_data import header_list, headersDict


def get_poi(df, extracted_data):
    table = Table(df)
    table.getTable(header_list)
    table.df[table.tableId] = table.df[table.tableId].replace(np.nan, -1)
    print(table.getListOfIndex(headersDict))
    data = table.extractData()
    extracted_data['numberOfPerformanceObligations'] = len(data)
    extracted_data['poi'] = data
    return extracted_data
