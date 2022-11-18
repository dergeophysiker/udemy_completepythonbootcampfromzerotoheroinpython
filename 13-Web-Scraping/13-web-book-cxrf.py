import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
page_num=12

#print(base_url.format(page_num))


res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
#print(soup)
products= soup.select(".product_pod")
example=products[0]
#print(example)
#print(len(soup.select(".product_pod")))
print('star-rating Three' in str(example))

ex1= example.select(".star-rating.Three")
print(ex1)

ex4= example.select('a')

print(ex4)


ex3= example.select('a')[1]
print(ex3)
print(ex3.text)


ex2= example.select('a')[1]['title']

print(ex2)

'''
two_start_titles=[]

for n in range(1,51):
    
    scrape_url=base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title=book.select('a')[1]['title']
            two_start_titles.append(book_title)

print(two_start_titles)
'''