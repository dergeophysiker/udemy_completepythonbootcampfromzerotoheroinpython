def swap(index1,index2,arr):
    temp=arr[index1]
    arr[index1]=arr[index2]
    arr[index2]=temp
    
def partition(arr,lo,hi):
    pivot = arr[hi]
    i=lo-1
    for j in range(lo,hi):
        if arr[j] <= pivot:
            i=i+1
            swap(i,j,arr)
            print(i)
    i=i+1
    correctpivotindex=i
    swap(i,hi,arr)
    return correctpivotindex   

def quick_sort_iterative(arr):
    stack=[]
    stack.append(0)
    stack.append(len(arr)-1)
    #print("initial stack: {}".format(stack))
    LOOP=0
    while stack:
        #print(stack.pop())
        hi=stack.pop()
        lo=stack.pop()
        print("partition values {} {}".format(lo,hi))
        pivind=partition(arr,lo,hi)
        print("pivot index: {} array {} stack {}".format(pivind,arr,stack))
        if hi-pivind >= 2: # check # of elements to right side of pivot same as pivind+1<h
            stack.append(pivind+1)
            stack.append(hi)

        if pivind-lo >= 2: #check # of elements to left side of pivot same as pivind-1>l
            stack.append(lo)
            stack.append(pivind-1)
        print(stack)    
        LOOP=LOOP+1
        print(LOOP)

#dumbarr=[5,4,3,2]
#dumbarr=[3,2,1]
#dumbarr=[4,23,16,13,47,111]
#dumbarr=[8,3,1,7,0,10,2]
#dumbarr=[10,8,7,3,2,1,0]
#dumbarr = [4, 3, 5, 2, 1, 3, 2, 3] 
#dumbarr=[4,3,33,432,433,433,433,-12,22,23,0,-21321]
#dumbarr=[4]
#dumbarr=[1,2,3,4,5,6,7,8,9,10] #- when the array is sorted
dumbarr=[10,9,8,7,6,5,4,3,2,1] #- when the array is reversed
#dumbarr=[1,1,1,1,1,1,1,1,1,1] #- when the array is the same values
#dumbarr=[1,1,1,2,2,2,3,3,3,3] #- when there are few and unique keys
#k=dumbarr.copy()
#result = partition(dumbarr,0,len(dumbarr)-1)
#print("pivot index: {} and partioned array={} and original array is {}".format(result,dumbarr,k))
quick_sort_iterative(dumbarr)
print(dumbarr)

'''
this= [0, 8, 7, 3, 2, 1, 10]
result=partition(this,1,6)
print(result)
print(this)
'''