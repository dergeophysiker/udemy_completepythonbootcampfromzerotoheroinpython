import requests
import bs4

#soup.select('#some_id')
#soup.select('.some_class')


result = requests.get("http://www.example.com")
type(result)
print(type(result))

print(result.text)

soup = bs4.BeautifulSoup(result.text,"lxml")
print(soup.select('title'))
k=soup.select('p')
print(k[0].getText())


res=requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')
#soup.select
print(soup.select('.toctext')[0])

resdeep = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(resdeep.text, 'lxml')
imgs = soup.select('.thumbimage')
print(imgs)
print("###############################################################################")
print("###############################################################################")
print("###############################################################################")

for item in imgs:
    print(item)

computer = soup.select('.thumbimage')[0]
print(computer)
print(computer['src'])
image_link = requests.get('https:'+computer['src'])
print(image_link.content)

f = open('my_computer_image.jpg','wb')
f.write(image_link.content)
f.close()




