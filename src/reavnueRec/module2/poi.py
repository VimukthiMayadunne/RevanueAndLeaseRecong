import pandas as pd
import numpy as np

from src.reavnueRec.module2.classes.Table import Table
from src.reavnueRec.support.table_data import header_list, headersDict
from src.reavnueRec.support.clear_buffer import clear_buffer

def get_poi(df, extracted_data):
    table = Table(df)
    table.getTable(header_list)
    table.df[table.tableId] = table.df[table.tableId].replace(np.nan, -1)
    table.getListOfIndex(headersDict)
    data = table.extractData()
    return extracted_data
