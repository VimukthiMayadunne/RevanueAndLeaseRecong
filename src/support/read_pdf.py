import PyPDF2


def read_pdf(path):
    f = open(path, 'rb')
    pdf_text = []
    pdf_reader = PyPDF2.PdfFileReader(f)
    for p in range(pdf_reader.numPages):
        page = pdf_reader.getPage(p)
        pdf_text.append(page.extractText())
    f.close()
    data = '.'.join(str(x) for x in pdf_text)
    return data
