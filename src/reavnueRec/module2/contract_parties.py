from spacy.matcher import Matcher

pattern_buyer = [[{'LOWER': 'site'}, {'LOWER': 'name'}, {'IS_PUNCT': True}],
                 [{'LOWER': 'buyer'}, {'LOWER': 'details'}]]
pattern_seller = [[{'LOWER': 'seller'}, {'LOWER': 'details'}, {'IS_PUNCT': True}],
                  [{'LOWER': 'seller'}, {'LOWER': 'details'}],[{'LOWER': 'sub'},
                {'IS_PUNCT': True},{'LOWER': 'contractor'}]]
pattern_person = [{"label": "PERSON", "pattern": [{'IS_TITLE': True}]}]


def findContractor(nlp, doc, ruler):
    matcher = Matcher(nlp.vocab)
    matcher.add("buyer", pattern_buyer)

    ruler.add_patterns(pattern_person)
    matches = matcher(doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        token_window = doc[end :end + 8]
        print(token_window.text)
        span = doc[start:end]  # The matched span
        print(match_id, string_id, start, end, span.text)
        for ent in token_window.ents:
            print("----------")
            print(ent)
            print("------")
            if (ent.label == 380 or ent.label == 383) and string_id == 'buyer':
                print("string matched")
                contractor = ent.text
                return contractor
            else:
                return "Contractor"
    return "ContractorName"

def findContractee(nlp, doc, ruler):
    matcher = Matcher(nlp.vocab)
    matcher.add("seller", pattern_seller)
    ruler.add_patterns(pattern_person)
    matches = matcher(doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        token_window = doc[end + 1:end + 18]
        for ent in token_window.ents:
            if (ent.label == 380 or ent.label == 383) and string_id == 'seller':
                contractee = ent.text
                return contractee
            else:
                return None
