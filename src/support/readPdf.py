import fitz


def readPdf(file):
    with fitz.open(file) as doc:
        text = ""
        for page in doc:
            text += page.getText()
        print(text)
        return text
