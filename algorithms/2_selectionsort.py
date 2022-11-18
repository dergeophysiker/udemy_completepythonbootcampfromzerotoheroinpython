#selction sort
# choose smallest element 

def findsmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index=i
    return smallest_index

def selectionsort(array1):
    sortarr=[]
    for i in range(len(array1)):
        smallest=findsmallest(array1)
        sortarr.append(array1.pop(smallest))
    return sortarr

nums=[-123,-123,-256,32,0,333,333,444,2,2,-3223,-999999,333]

k=findsmallest(nums)
print(k)
b=selectionsort(nums)
print(b)