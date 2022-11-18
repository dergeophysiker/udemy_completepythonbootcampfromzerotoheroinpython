from os import system
def create_cubes(n):
    result=[]
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10))

for x in create_cubes(10):
    print(x)

def create_cubes_yield(n):
    for x in range(n):
        yield x**3

for y in create_cubes_yield(10):
    print(y*0)

def gen_fibo(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b=b,a+b


for number in gen_fibo(10):
    print(number)

#########################################################################
system('cls')
def simple_gen():
    for x in range(3):
        yield x
    
for number in simple_gen():
    print(number) # for loop catches the stop iteration error and catches it

g=simple_gen()
print(g)
print(next(g))
print(next(g))
print(next(g)) # last value yield. after this it stops iteration
#########################################################################
system('cls')

s= 'hello'
for letter in s:
    print(letter)

s_iter=iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
