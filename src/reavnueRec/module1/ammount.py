from spacy.matcher import Matcher
from src.reavnueRec.support.c_to_f import c_to_f
import re

pattern_ammount = [[{'LOWER': 'payment'},
                   {'LOWER': 'information'},
                   {'IS_PUNCT': True}],[{'LOWER': 'payment'},
                   {'LOWER': 'information'}]]

regex = r"(?:Rs\.?|INR)\s*(\d+(?:[.,]\d+)*)|(\d+(?:[.,]\d+)*)\s*(?:Rs\.?|INR)"


def findAmount(nlp, doc, ruler):
    matcher = Matcher(nlp.vocab)
    matcher.add("ammount", pattern_ammount)
    matches = matcher(doc)
    for match_id, start, end in matches:
        token_window = doc[end + 1:end + 18]
        matches = re.finditer(regex, token_window.text)
        for  matchNum, match in enumerate(matches, start=1):
            value = match.group()
            value = c_to_f(value)
            return value

