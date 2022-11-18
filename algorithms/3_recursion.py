def countdown(i):
    print(i)
    if i == 0:
        return
    else:
        countdown(i-1)

#countdown(100)


def fact(i):
    if i==1:
        return 1
    else:
        return i * fact(i-1)

#print(fact(500))


x=[1,2,3]
print(x)
x.pop()
print(x)

arr=list(range(1,101))
print(arr)

def recsum(arr):
    if not arr:
        return 0
    else:
        return arr.pop() + recsum(arr)

y = recsum(arr)
print(y)
