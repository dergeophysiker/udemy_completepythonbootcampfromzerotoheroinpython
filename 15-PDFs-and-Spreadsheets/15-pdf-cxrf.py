
'''
import csv

# open the file
data = open('example.csv',encoding='utf-8')

#csv.read
csv_data = csv.reader(data)
#reformat
data_lines=list(csv_data)
print(data_lines[0])
print(len(data_lines))

for line in data_lines[:5]:
    print(line)

print(data_lines[10])
print(data_lines[10][3])
all_emails=[]

for line in data_lines[1:]:
    all_emails.append(line[3])

print(all_emails)

full_name=[]
for line in data_lines[1:]:
    full_name.append(line[1]+' '+line[2])

print(full_name)

file_to_output=open('to_save_file.csv',mode='w',newline='')

csv_writer=csv.writer(file_to_output,delimiter=',')

csv_writer.writerow(['a','b','c'])
csv_writer.writerows([[1,2,3,4],[4,5,6]])
file_to_output.close()

f = open('to_save_file.csv',mode='a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['1','2','3'])
f.close()
'''
#########################################################################################
import PyPDF2
'''
f=open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
print(page_one_text)
f.close()
'''

f=open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)
print(type(first_page))


pdf_output = open('SomeBrandNew.pdf','wb')

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)

#pdf_output = open('SomeBrandNew.pdf','wb')

pdf_writer.write(pdf_output)
f.close()
#f.close()

pdf_output.close()

f = open('Working_Business_Proposal.pdf','rb')
pdf_text=[]
pdf_reader = PyPDF2.PdfFileReader(f)
for num in range(pdf_reader.numPages):
    page=pdf_reader.getPage(num)
    pdf_text.append(page.extractText())

print(pdf_text[0])