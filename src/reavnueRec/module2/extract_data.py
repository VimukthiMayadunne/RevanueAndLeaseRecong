import spacy
from spacy import displacy

from src.reavnueRec.module2.amount import findAmount
from src.reavnueRec.support.c_to_f import c_to_f
from src.support.spac_support import show_ents

from src.reavnueRec.module2.contract_parties import findContractor,findContractee
from src.reavnueRec.module2.duration import duration
nlp = spacy.load('en_core_web_lg')
ruler = nlp.add_pipe("entity_ruler")

def extract_data(data,extracted_data):
    doc = nlp(data)
    extracted_data['contractor'] = findContractor(nlp, doc, ruler)
    extracted_data['contractee'] = findContractee(nlp, doc, ruler)
    extracted_data = duration(nlp,doc,ruler,extracted_data)
    extracted_data['amount'] = c_to_f(findAmount(nlp, doc, ruler))
    print(extracted_data)
    return extracted_data
