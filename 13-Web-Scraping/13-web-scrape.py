import requests
import bs4
import pdb
import re

base_url = 'http://quotes.toscrape.com/page/{}/'
#http://quotes.toscrape.com/page/1/
error_text="No quotes found!"

match=None
counter=1
list_authors=[]
set_authors=set()

while match == None:
    res=requests.get(base_url.format(counter))
    print(res.status_code)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    match=re.search(error_text,soup.get_text())
    print(match)
    print(counter)
    
    authors = soup.select(".author")
#print(authors)
    for author in authors:
        print(author.text)
        list_authors.append(author.text)
        set_authors.add(author.text)    
    counter+=1

print(list_authors)
print(set_authors)
print(len(set_authors))
print(len(set(list_authors)))
'''
#print(soup)

authors = soup.select(".author")
#print(authors)

for author in authors:
    print(author.text)

quotes = soup.select(".text")
for quote in quotes:
    print(quote)
    print(type(quote))
    print(quote.text)

quotes2 = soup.select(".quote")
for quote in quotes2:
    tag=quote.select('.text')
    print(type(tag))
    print(type(tag[0]))
    print(tag[0].text)

#with open("") as f:

tenquotes = soup.select(".col-md-4.tags-box")
quol=(tenquotes[0].select(".tag"))

for q in quol:
    print(q.text)
'''

