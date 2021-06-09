import spacy
nlp = spacy.load('en_core_web_sm')

def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.label)
            print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))
    else:
        print('No named entities found.')

def remove_whitespace_entities(doc):
    doc.ents = [e for e in doc.ents if not e.text.isspace()]
    return doc

def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == ',':
            doc[token.i+1].is_sent_start = True
    return doc





