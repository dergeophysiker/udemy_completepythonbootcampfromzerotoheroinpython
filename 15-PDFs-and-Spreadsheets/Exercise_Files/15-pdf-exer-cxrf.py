import csv
import PyPDF2
import re

########################################working code########################################
'''

# open the file
data = open('find_the_link.csv',encoding='utf-8')

#csv.read
csv_data = csv.reader(data)
#reformat
data_lines=list(csv_data)

address=[]
for index,line in enumerate(data_lines[:]):
    print(line[index])
    address.append(line[index])
    #print(index)
print(''.join(address))
'''
########################################working code########################################


f = open('Find_the_Phone_Number.pdf','rb')
pdf_text=[]
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)

phone_pattern = re.compile(r'(\d{3}).(\d{3}).(\d{4})')

phone_pattern2 = re.compile(r'\d\d\d.\d\d\d.d\d\d\d')


matches=[]
matchtext=[]

for num in range(pdf_reader.numPages):
    page=pdf_reader.getPage(num)
    pdf_text.append(page.extractText())
    results = re.search(phone_pattern, page.extractText())
    results2=re.findall(phone_pattern,page.extractText())
    if results is not None:
        matches.append(results)
    print(results)
    print(results2)

print(len(pdf_text))
print(matches)
print(matches[0].group())
#print(pdf_text[0])
