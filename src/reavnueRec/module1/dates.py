from spacy.matcher import Matcher

pattern_amounts = [{'LOWER': 'payment'}, {'LOWER': 'information'}, {'IS_PUNCT': True}]
pattern_singleDay = [{'LOWER': 'date'}, {'LOWER': 'of'}, {'LOWER': 'transaction'}, {'IS_PUNCT': True}]
pattern_date = [{"label": "DATE", "pattern": [{'IS_TITLE': True}]}]


def find_dates(nlp, doc, ruler, extracted_data):
    interval_payment = True
    matcher = Matcher(nlp.vocab)
    matcher.add("amount", [pattern_amounts])
    matcher.add("single_day", [pattern_singleDay])

    ruler.add_patterns(pattern_date)
    matches = matcher(doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]
        if string_id == 'single_day':
            interval_payment = False

    if not interval_payment:
        extracted_data['intervalPayment'] = False
        extracted_data['interval'] = 1
        extracted_data['duration'] = 1
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]
            token_window = doc[end + 1:end + 22]
            for ent in token_window.ents:
                if ent.label == 391 and string_id == 'amount':
                    extracted_data['transDate'] = ent.text
                    extracted_data['single_day'] = True
        return extracted_data
    else:
        extracted_data['intervalPayment'] = True
        extracted_data['interval'] = 1
        extracted_data['duration'] = 12
        return extracted_data
