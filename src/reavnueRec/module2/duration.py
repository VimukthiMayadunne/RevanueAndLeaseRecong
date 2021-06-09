import datetime
from spacy.matcher import Matcher
from dateutil.parser import parse
from src.reavnueRec.support.calculate_delta import monthdelta

pattern_commence = [ [{'LOWER': 'date'},
           {'LOWER': 'on'},
           {'LOWER': 'commence'}]]
pattern_end = [[{'LOWER': 'end'},
           {'LOWER': 'date'},
           {'IS_PUNCT': True}]]


def duration(nlp, doc, ruler,extracted_data):
    matcher = Matcher(nlp.vocab)
    matcher.add("commence", pattern_commence)
    matcher.add("end", pattern_end)
    matches = matcher(doc)
    print(len(matches))
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        token_window = doc[end :end + 6]
        for ent in token_window.ents:
            if ent.label == 391 and string_id == 'commence':
                commence_date = ent.text
                commence_date = commence_date.replace('th day of ', ' ')
                commence_date = commence_date.replace('st day of ', ' ')
                commence_date = commence_date.replace('nd day of ', ' ')
                commence_date = commence_date.replace('rd day of ', ' ')
                commence_date = commence_date.replace(' ', ' ')
                commence_dt = parse(commence_date)
            if ent.label == 391 and string_id == 'end':
                end_date = ent.text
                end_date = end_date.replace('th day of ', ' ')
                end_date = end_date.replace('st day of ', ' ')
                end_date = end_date.replace('nd day of ', ' ')
                end_date = end_date.replace('rd day of ', ' ')
                end_date = end_date.replace(' ', ' ')
                end_dt = parse(end_date)
    print(commence_date,end_date)
    print(commence_dt,end_dt)
    duration_monts = monthdelta(commence_dt,end_dt)
    print(duration_monts)
    extracted_data['intervalPayment'] = False
    extracted_data['interval'] = 1
    extracted_data['duration'] = duration_monts
    extracted_data['commence_date'] = commence_date
    extracted_data['end_date'] = end_date
    return extracted_data


