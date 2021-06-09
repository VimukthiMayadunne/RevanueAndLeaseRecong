import spacy
from spacy.matcher import Matcher
from spacy.language import Language


@Language.component("set_custom_boundaries")
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == ",":
            doc[token.i + 1].is_sent_start = True
    return doc


tagTypes = [15794550382381185553, 13927759927860985106, 14200088355797579614, 15308085513773655218]
# SELLER'S RESPONSIBILITES:
pattern_res = [[{'LOWER': 'seller'},
                {'ORTH': "'S"},
                {'LOWER': 'responsibilites'}]]


def find_poi(nlp, doc, ruler, extracted_data):
    base_doc = nlp("The Contractor agrees to provide the contractee with the product.")
    nlp.add_pipe("set_custom_boundaries", before="parser")
    matcher = Matcher(nlp.vocab)
    matcher.add("buyer", pattern_res)
    matches = matcher(doc)
    for match_id, start, end in matches:
        token_window = doc[end + 1:end + 55]
        newDoc = token_window.text
        newNlp = nlp(newDoc)
        spans = list(newNlp.sents)
        for sen in spans:
            temp_count = 0
            temp_doc = sen.text
            temp_nlp = nlp(temp_doc)
            tag_counts = temp_nlp.count_by(spacy.attrs.TAG)
            for k, v in sorted(tag_counts.items()):
                if k in tagTypes:
                    temp_count += 1
            doc_simlirity = temp_nlp.similarity(base_doc)
            if doc_simlirity >= 0.8 and temp_count >= 4:
                extracted_data['numberOfPerformanceObligations'] += 1
                if extracted_data["single_day"]:
                    tempt = {"name": temp_nlp[-3:-1].text,
                             "StandAlonePrice": extracted_data["amount"],
                             "Recurent": False,
                             "whenToPerform": 0
                             }
                    print(tempt)
                    extracted_data['poi'].append(tempt)
                    print(extracted_data['poi'])
    return extracted_data
