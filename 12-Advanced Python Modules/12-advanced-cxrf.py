from collections import Counter,defaultdict
from collections import namedtuple
from os import system
import os
import shutil

mylist=[1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]

counted=Counter(mylist)
print(counted)

letters='aaaaaaaaaaabbbbbbbbbvcccccccddddddddeeeeeeeeesasd'

counted=Counter(letters)
print(counted)

print(counted.most_common(2))

print(list(counted))
d=defaultdict(lambda: 0)
#d={'a':1}
#print(d['a'])
d['correct']=100
print(d['wrong key'])
print(d['correct'])

mytuple = (10,20,30)
print(mytuple[2])


Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(5, 'husky','sam')
print(sammy)

print(sammy.age)
#########################################################################

system('cls')
print(os.getcwd())

f=open('practice.txt','w+')
f.write('this is a test string')
f.close()

#print(os.listdir())
#print(os.listdir('c:\\users'))
#shutil.move('practice.txt','new')
#os.unlink('new')
'''
for folder, subfolders, files in os.walk("C:\\Users\\CCCC\\OneDrive - XX\\Documents\\python\\bootcamp\\git\\12-Advanced Python Modules\\Example_Top_Level"):
    print(f"currently looking at {folder}")
    print("\n")
    print("the subfolders are: ")
    for subfold in subfolders:
        print(f"subfolder: {subfold}")
'''
for folder, subfolders, files in os.walk("C:\\Users\\CCCC\\OneDrive - XX\\Documents\\python\\bootcamp\\git\\12-Advanced Python Modules\\Example_Top_Level"):
    print(f"{folder}, {subfolders},{files}")


#########################################################################
import datetime
#from datetime import datetime

mytime = datetime.time(2, 20)
print(mytime.minute)
print(mytime.hour)
print(mytime)
print(type(mytime))

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.ctime())
print(type(today))




#from datetime import datetime
#mydatetime= datetime(2021,10,3,14,20,1)
mydatetime = datetime.datetime(2021,10,3,14,20,1)
print(type(mydatetime))
print(mydatetime)


mydatetime2 = datetime.datetime(2021,10,21,22)
print(mydatetime2.weekday())

start=datetime.datetime(2021,11,3,20)
end=datetime.datetime(2020,11,3,10)

diff= start-end
print(diff.total_seconds())
#########################################################################


import math

value=4.35
print(math.floor(value))
print(math.ceil(value))
print(round(value)) # 4.5 rounds to 4
print(round(5.5)) # rounds to 6
# rounds to nearest even number if .5 split
#math.pi
#math.inf
#math.nan
#math.e
#Numpy
print(math.log(math.e))
print(math.log(100,10))
#math.sin(10)=-.54 radians
#math.degrees(pi/2) = 90
#math.radians(180) = 3.14159
import random
#random.seed(42)
print(random.randint(0,100))

mylist=list(range(0,20))
print(random.choice(mylist))

# sample with replacement
print(random.choices(population=mylist, k=10))

random.shuffle(mylist)
print(mylist)
print(random.uniform(a=0,b=100))
print(random.gauss(mu=0,sigma=1))
#########################################################################
system('cls')
import pdb

x=[1,2,3]
y=2
z=3

result1 = y + z
#pdb.set_trace()
#result2 = y + x
#########################################################################
system('cls')
#phone number (555)-555-5555  
# regex pattern r"(\d\d\d)-\d\d\d-\d\d\d\d
# r"(\d{3})
text = "the agents phone # is 408-555-1234"
import re
pattern="phone"
#pattern="NOT IN TEXT"
match=re.search(pattern,text)
print(match)
match.span()
match.start()
match.end()
text2="my phone onece, my phone twice"
match2 = re.search('phone',text2)
print(match2)
pdb.set_trace()
matches = re.findall('phone',text2)
print(matches)
for match in re.finditer('phone',text2):
    print(match.span())
    print(match.group())
pdb.set_trace()
system('cls')

text3="my phone number is 408-555-1234"
#phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text3)
#phone = re.search(r'\d{3}-\d{3}-\d{4}',text3)
#print(phone)
#print(phone.group())

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text3)
print(phone_pattern)
print(results)
print(results.group())
print(results.group(1))

system('cls')

s=re.search(r'cat|dog','the dog is here')
print(s)
s1 = re.findall(r'...at','the cat in the hat sat there went splat')
print(s1)
s2=re.findall(r'\d$|^\d','2 is a number 2')
print(s2)

phrase ="there are d3 numbers 34 inside 5 this sentence 53s"
pattern=r'[^\d]'
pattern1=r'[^\d]+'

s3=re.findall(pattern,phrase)
print(s3)
s4=re.findall(pattern1,phrase)
print(s4)

test_phrase = "this is a string! but it has punctuation. how can we remove it?"
clean=re.findall(r'[^!.?]+', test_phrase)
clean2=re.findall(r'[^!.? ]+', test_phrase)

print(clean)
print(clean2)
print(' '.join(clean))

text="only find the long-ish hypen-words in this sentence. but you dont know how long they are as hypen-words"
pattern3=r'[\w]+'

result3=re.findall(pattern3,text)
print(result3)

pattern4=r'[\w]+-[\w]+'
result4=re.findall(pattern4,text)
print(result4)

textone= 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

print(re.search(r'cat(fish|nap|claw)',textone))
print(re.search(r'cat(fish|nap|claw)',texttwo))
print(re.search(r'cat(fish|nap|claw)',textthree))

#########################################################################
system('cls')

