from src.reavnueRec.module3.data_from_nlp import extract_data_nlp
from src.reavnueRec.module3.poi import getpoi
from src.reavnueRec.support.api_request import send_request
from src.support.read_pdf import read_pdf


def get_contract_details(path, df, extracted_data):
    data = read_pdf(path)
    extracted_data = extract_data_nlp(data, extracted_data)
    extracted_data = getpoi(df, extracted_data)
    send_request(extracted_data)
