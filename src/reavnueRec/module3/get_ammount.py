from spacy.matcher import Matcher
from src.reavnueRec.support.c_to_f import c_to_f

pattern_amount = [{'LOWER': 'provisional'},
           {'LOWER': 'sum'},{'LOWER': 'is'}]

def find_amount(nlp, doc, ruler):
    matcher = Matcher(nlp.vocab)
    matcher.add("amount", [pattern_amount])
    matches = matcher(doc)
    print(len(matches))
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        token_window = doc[end + 1:end + 18]
        span = doc[start:end]  # The matched span
        print(match_id, string_id, start, end, span.text)
        for ent in token_window.ents:
            if ent.label == 397 and string_id == 'amount':
                amount = ent.text
                amount = c_to_f(amount)
                return amount

