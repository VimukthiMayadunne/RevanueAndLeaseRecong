from spacy.matcher import Matcher
from src.reavnueRec.support.c_to_f import c_to_f

pattern_duration = [{'LOWER': 'construction'},
           {'LOWER': 'duration'},
           {'IS_PUNCT': True}]
def find_duration(nlp, doc, extracted_data):
    matcher = Matcher(nlp.vocab)
    matcher.add("duration", [pattern_duration])
    matches = matcher(doc)
    print(len(matches))
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        token_window = doc[end + 1:end + 18]
        span = doc[start:end]  # The matched span
        print(match_id, string_id, start, end, span.text)
        for ent in token_window.ents:
            print( ent.text , ent.label_ , ent.label)
            if ent.label == 391 and string_id == 'duration':
                duration = ent.text
                extracted_data['intervalPayment'] = True
                extracted_data['interval'] = 1
                extracted_data['interval'] = 1
                extracted_data['duration']  = c_to_f(duration)
            return extracted_data
