print(hex(12))
bin(128)
print(bin(234234232342323))
print(pow(2,4,3)) # = 16 mod 3 
print(abs(3))
print(round(4.5))

######################################

s = 'Helloworld Fun'
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.count('o'))
print(s.find('o',5))
print(s.center(21,'z'))
print(s.center(20,'z'))
print('hell\t34'.expandtabs())
print(s.isalnum())
print(s.isalpha())
print(s.islower())
print(s.isspace())
print(s.istitle())
#s.isupper()
#s.endswith('o')

print(s.split('o'))
print(s.partition('o'))

######################################

ss=set()
ss.add(1)
ss.add(2)
print(ss)
ss.clear()
print(ss)
ss={1,2,3}
sc=ss.copy()
ss.add(4)
print(sc)
#sc.clear()
print(sc)
print(ss)

print(ss.difference(sc))

s1={0,1,2,3,4,34}
s2={1,23,4,34,99}

#s1.difference_update(s2) # return first set s1 after removing all elements in s1 also found in s2 (1)
#print(s1)

s2.discard(23)
print(s2)

print(s1.intersection(s2))
print(s2.intersection(s1))
print(s1)
print(s2)
print("intersection upate")
s1.intersection_update(s2)
print(s1)
print(s2)
print("intersection upate")
print(s2.intersection_update(s1))
print(s2)
print(s1)

sa = {1,2}
sb={1,2,4,5}
sc={1,2,5,99}

print(sa.isdisjoint(sb))
print(sa.issubset(sb))
print(sa.issuperset(sb))

print(sa.symmetric_difference(sb))
print(sc.symmetric_difference(sa))
#c = {[],[]}
#print(len(c))
#print(c == set())

print(sa.union(sb))
print(sa.union(sc))
print(sa.update(sc))
print(sa)

######################################


d={'k1':1,'k2':2}
print(d)
print({x:x**2 for x in range(10)})
print({k:v+2 for k,v  in zip(['a','b'], range(2))})

for k in d.items():
    print(k)

for k in d.keys():
    print(k)

for k in d.values():
    print(k)

######################################

l = [1,2,3,3]
l.append(4)

print(l)

print(l.count(3))

x=[1,2,3]
y=[6,7,8]
x.append([4,5])
print(x)

x.extend(y)
print(x)

print(l.index(2))

l.insert(0,'inserted')
print(l)

ele = l.pop(0)  # pop with index
print(ele)
print(l)
l.remove(3)  # remove 1st ocurence of value
print(l)

l.reverse()
print(l)
l.sort()
print(l)
