import PyPDF2

def extract_text(pdf_file):

    text = ""

    with open(pdf_file, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text