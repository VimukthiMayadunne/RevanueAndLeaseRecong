import tabula

from src.reavnueRec.module3.main_app import get_contract_details
from src.reavnueRec.module1.graph_main import graph_main
from src.reavnueRec.support.objectmodel import extracted_data
from src.reavnueRec.module2.main_app import summary_data

file_path = "/home/vimukthi/Desktop/Contracts/p3.pdf"

dfs = tabula.read_pdf(file_path, stream=True, multiple_tables=True, pages='all')

if len(dfs) >= 1:
    print("Tables Exits")
    if dfs[0].columns[0] == 'Contract Summary':
        print('Summary Table Exists');
        summary_data(dfs,extracted_data)
    else:
        print('Tables Exist');
        get_contract_details(file_path, dfs, extracted_data)
else:
    print("Paragraph Based Contract")
    graph_main(file_path, extracted_data)
