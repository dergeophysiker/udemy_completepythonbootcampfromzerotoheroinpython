# Python program for implementation of Quicksort  

# This function is same in both iterative and recursive 
def partition(arrp, l, h):
    i = ( l - 1 ) 
    x = arrp[h] 
    #print(id(arrp))
    #arrp=[1,2,3]
    #print(id(arrp))
    for j in range(l, h): 
        print("index {} of {}. Array is {}.".format(j,h-1,arrp))
        if   arrp[j] <= x: 
            # increment index of smaller element 
            i = i + 1
            print("{} <= {} so swap {} and {}".format(arrp[j],x,arrp[i],arrp[j]))
            arrp[i], arrp[j] = arrp[j], arrp[i]
            
    print("last step swap {} and {} ".format(arrp[i+1],arrp[h]))        
    arrp[i + 1], arrp[h] = arrp[h], arrp[i + 1] 
    print("partitioned array: {}".format(arrp))
    return (i + 1) 
  
# Function to do Quick sort 
# arr[] --> Array to be sorted, 
# l  --> Starting index, 
# h  --> Ending index 
def quickSortIterative(arr, l, h): 
    #print(id(arr))
    # Create an auxiliary stack 
    size = h - l + 1
    stack = [0] * (size) 
  
    # initialize top of stack 
    top = -1
  
    # push initial values of l and h to stack 
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 
    LOOP=0
    # Keep popping from stack while is not empty 
    while top >= 0: 
    
        # Pop h and l
        print("stack before pop: {} top= {}".format(stack,top))
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
        print("stack after pop: {} top= {}".format(stack,top))
        print("popped h: {} and l: {}".format(h,l))
        print("calling partition: l={} and h={}".format(l,h))
        print("")
        # Set pivot element at its correct position in 
        # sorted array 
        p = partition( arr, l, h ) 
        print("partion call produced pivot at position {}".format(p))
        # If there are elements on left side of pivot, 
        # then push left side to stack 
        print(" p-1 > l? {} > {} = {}".format(p-1,l,p-1>l))
        if p-1 > l: 
            print("elements on left side of pivot (p-1>l) {} > {}".format(p-1,l))
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot, 
        # then push right side to stack 
        print(" p+1 < h? {} < {} = {}".format(p+1,h,p+1<h))
        if p + 1 < h:
            print("elements on right side of pivot (p+1<h) {} < {}".format(p+1,h))
            print("")
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 
        LOOP=LOOP+1
        print(LOOP)  
# Driver code to test above 
#arr=[5,4,3,2]
#arr=[4,23,16,13,47,111]
#arr=[8,3,1,7,0,10,2]
#=[10,8,7,3,2,1,0]
#arr = [4, 3, 5, 2, 1, 3, 2, 3] 
#arr=[4,3,33,432,433,433,433,-12,22,23,0,-21321]
arr=[10,9,8,7,6,5,4,3,2,1]
n = len(arr) 
quickSortIterative(arr, 0, n-1)
print("final result: {}".format(arr))
#print ("Sorted array  is not:") 

'''
for i in range(n): 
    print ("% d" % arr[i]), 
  
x = [0, 1]
i = 0
i, x[i] = 1, 2         # i is updated, then x[i] is updated
print(x)


def reassign(list):
  #return [88, 88]
    list = [99,99]

def append(list):
  list.append(100)

list = [0]

#list = reassign(list)
#reassign(list)
#print(list)
append(list)
print(list)
print("next")
listA = [0]
listB = listA
listB.append(-1)
print(listA)
print(listB)

lst = [1, 2]
def f(lst):
    lst = lst + [3]  # seems pass by value
#     lst += [3]  # strange! same as above but seems pass by reference
    #lst = lst.append(3)  # seems pass by reference
    return lst
f(lst)  
print(lst)
'''