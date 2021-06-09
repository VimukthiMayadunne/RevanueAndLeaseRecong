import spacy

from src.reavnueRec.support.get_text_file import opentxt
from src.reavnueRec.support.objectmodel import extracted_data
from src.reavnueRec.module1.m1 import findContractor, findContractee
from src.reavnueRec.module1.ammount import findAmount
from src.reavnueRec.module1.dates import find_dates
from src.reavnueRec.module1.poi import find_poi
from src.reavnueRec.support.api_request import send_request
from src.reavnueRec.support.c_to_f import c_to_f


nlp = spacy.load('en_core_web_lg')
data = opentxt('/home/vimukthi/FYP/RevanueAndLeaseRec/src/contracts/Allion.txt')
doc = nlp(data)
ruler = nlp.add_pipe("entity_ruler")

extracted_data['contractor'] = findContractor(nlp, doc, ruler)
extracted_data['contractee'] = findContractee(nlp, doc, ruler)
extracted_data['amount'] = c_to_f(findAmount(nlp, doc, ruler))
extracted_data = find_dates(nlp,doc,ruler,extracted_data)
extracted_data = find_poi(nlp, doc, ruler, extracted_data)

print(extracted_data)

send_request(extracted_data)

