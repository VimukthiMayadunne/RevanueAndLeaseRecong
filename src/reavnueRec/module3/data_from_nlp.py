import spacy
from spacy import displacy

from src.reavnueRec.module3.get_contract_parties import findContractee, findContractor
from src.reavnueRec.module3.get_ammount import find_amount
from src.reavnueRec.module3.get_duration import find_duration
nlp = spacy.load('en_core_web_lg')
ruler = nlp.add_pipe("entity_ruler")

def extract_data_nlp(text,extracted_data):
    doc = nlp(text)
    extracted_data['contractor'] = findContractor(nlp, doc, ruler)
    extracted_data['contractee'] = findContractee(nlp, doc, ruler)
    extracted_data['amount'] = find_amount(nlp, doc, ruler)
    extracted_data = find_duration(nlp,doc,extracted_data)
    print(extracted_data)
    return extracted_data

