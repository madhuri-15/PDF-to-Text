#! python3
# pdfTotext.py - Convert pdf files into text files.

from PyPDF2 import PdfFileReader 

pdfFile = open("sample.pdf", 'rb')

pdfReader = PdfFileReader(pdfFile)
pages = pdfReader.numPages
print(pages)

# create a new text file.
textFile = open("text.txt", 'w')

for page in range(pages):
    pageObj = pdfReader.getPage(page)
    text = pageObj.extractText()
    textFile.write(text)

textFile.close()
pdfFile.close()
    

