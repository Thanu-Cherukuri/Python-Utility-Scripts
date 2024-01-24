'''Pdf files processing using python
'''
import sys
import PyPDF2
with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)

with open('twopage.pdf', 'rb') as file2:
    reader2 = PyPDF2.PdfFileReader(file2)
    print(reader2.numPages)
    print(reader2.getPage(0))  # Accessing page 1
    print(reader2.getPage(1))  # Accessing Page 2

    page = reader2.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

# Merging two pdf's:

pdf_files = sys.argv[1:]


def pdf_combiner(pdf_list):
    '''Function performs merging a list of pdfs'''
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('combiner.pdf')


pdf_combiner(pdf_files)

# Watermark a pdf:
template = PyPDF2.PdfFileReader(open('combiner.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()
for pg_no in range(template.getNumPages()):
    page = template.getPage(pg_no)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    with open('watermarked_op.pdf', 'wb') as file3:
        output.write(file3)
