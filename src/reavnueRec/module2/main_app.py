import tabula

from src.reavnueRec.module2.extract_data import extract_data
from src.reavnueRec.module2.poi import get_poi
from src.reavnueRec.support.objectmodel import extracted_data
from src.reavnueRec.support.clear_buffer import clear_buffer

file_path = "/home/vimukthi/Desktop/p2.pdf"

dfs = tabula.read_pdf(file_path, stream=True, multiple_tables=True, pages='all')

if dfs[0].columns[0] == 'Contract Summary':

    print('Summary Table Exists');
    lst = []
    for index, row in dfs[0].iterrows():
        temp_data = row.values
        lst.append(str(temp_data))
    data_buffer = '.'.join(str(x) for x in lst)
    data_buffer = clear_buffer(data_buffer)
    extracted_data = extract_data(data_buffer,extracted_data)
    extracted_data = get_poi(dfs,extracted_data)
