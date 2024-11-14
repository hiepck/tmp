from pypdf import PdfReader

reader = PdfReader('./list.pdf')

meta = reader.metadata

print(meta)