import spacy
from spacy.matcher import Matcher
from spacy import displacy
from src.reavnueRec.support.get_text_file import opentxt
from src.reavnueRec.support.objectmodel import extracted_data
from src.support.spac_support import show_ents
from src.support.spac_support import remove_whitespace_entities

nlp = spacy.load('en_core_web_lg')

matcher = Matcher(nlp.vocab)
ruler = nlp.add_pipe("entity_ruler")

data = opentxt('/home/vimukthi/FYP/RevanueAndLeaseRec/src/contracts/Allion.txt')
doc = nlp(data)

pattern_buyer = [{'LOWER': 'buyer'}, {'LOWER': 'details'}, {'IS_PUNCT': True}]
matcher.add("buyer", [pattern_buyer])
pattern_seller = [{'LOWER': 'seller'}, {'LOWER': 'details'}, {'IS_PUNCT': True}]
matcher.add("seller", [pattern_seller])
pattern_person = [{"label": "PERSON", "pattern": [{'IS_TITLE': True}]}]
ruler.add_patterns(pattern_person)

matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    token_window = doc[end + 1:end + 18]
    for ent in token_window.ents:
        if ent.label == 380 and string_id == 'buyer':
            extracted_data['contractor'] = ent.text
        elif ent.label == 380 and string_id == 'seller':
            extracted_data['contractee'] = ent.text

print(extracted_data)

# displacy.serve(doc, style='ent')
# show_ents(doc)
# spans = list(doc.sents)
# displacy.serve(spans, style='ent', options={'distance': 110})
