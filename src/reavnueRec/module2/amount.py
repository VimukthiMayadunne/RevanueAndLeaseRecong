from spacy.matcher import Matcher
import re

pattern_amount = [[{'LOWER': 'total'},
                  {'LOWER': 'contract'},
                  {'LOWER': 'price'}],[{'LOWER': 'total'},
                  {'LOWER': 'installation'},
                  {'LOWER': 'charges'}]]

regex = r"(?:Rs\.?|INR)\s*(\d+(?:[.,]\d+)*)|(\d+(?:[.,]\d+)*)\s*(?:Rs\.?|INR)"


def findAmount(nlp, doc, ruler):
    matcher = Matcher(nlp.vocab)
    matcher.add("amount", pattern_amount)
    matches = matcher(doc)
    for match_id, start, end in matches:
        token_window = doc[end :end + 6]
        print(token_window.text)
        matches = re.finditer(regex, token_window.text)
        for matchNum, match in enumerate(matches, start=1):
            print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
            value = match.group()
        return value
