import spacy

from src.reavnueRec.module1.ammount import findAmount
from src.reavnueRec.module1.dates import find_dates
from src.reavnueRec.module1.m1 import findContractor, findContractee
from src.reavnueRec.module1.poi import find_poi
from src.support.read_pdf import read_pdf


def graph_main(path, extracted_data):
    data = read_pdf(path)
    print(data)
    nlp = spacy.load('en_core_web_lg')
    doc = nlp(data)
    ruler = nlp.add_pipe("entity_ruler")
    extracted_data['contractor'] = findContractor(nlp, doc, ruler)
    extracted_data['contractee'] = findContractee(nlp, doc, ruler)
    extracted_data['amount'] = findAmount(nlp, doc, ruler)
    extracted_data = find_dates(nlp, doc, ruler, extracted_data)
    extracted_data = find_poi(nlp, doc, ruler, extracted_data)

    print(extracted_data)
    #send_request(extracted_data)

