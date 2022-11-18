
#arr=list(range(1,101))
arr=[4,3,33,432,433,433,433,-12,22,23,0,-21321]
#arr=[5]
#arr=[]

print(arr)
#####################################################################
## problem 4.1

def rec_sum(arr):
    if not arr:
        return 0
    else:
        return arr.pop() + rec_sum(arr)

#y = recsum(arr)
#print(y)
#####################################################################

## problem 4.2

def rec_count(arr):
    if not arr:
        return 0
    else:
        arr.pop()
        return 1 + rec_count(arr)
#z=rec_count(arr)
#print(z)

#####################################################################

## problem 4.3

def find_max(arr):
    max_guess=arr[0]
    max_guess_index = 0
    for n in range(1,len(arr)):
        if max_guess < arr[n]:
            max_guess= arr[n]
            max_guess_index=n
    return max_guess_index
#w=find_max(arr)
#print(w)
#####################################################################

## problem 4.4

def binary_search(arr,item,L,R):
    mid=(L+R)//2
    if L <= R:
        guess=arr[mid]
        if guess==item:
            return mid
        elif guess < item:
            return binary_search(arr,item,mid+1,R)
        else:
            return binary_search(arr,item,L,mid-1)
    else:
        return -1

#arr.sort()
print(arr)
#value=0
#value=binary_search(arr,5,0,len(arr)-1)
#print(value)
#value=binary_search(arr,6,0,len(arr)-1)
#print(value)
#####################################################################
def quicksort(arr):
    if len(arr) < 2:
        if arr:
            return arr
        else:
            return []
    else:
        pivot=arr[0]
        #print(pivot)
        less=[i for i in arr[1:] if i <= pivot]
        greater=[i for i in arr[1:] if i > pivot]
        print("{} + {} + {}".format(less,pivot,greater))
        return quicksort(less) + [pivot] + quicksort(greater)

arr=[6,5,4,3,2,1]
sorted=quicksort(arr)
print(sorted)

arr=[1,2,3,4,5,6]
sorted=quicksort(arr)
print(sorted)