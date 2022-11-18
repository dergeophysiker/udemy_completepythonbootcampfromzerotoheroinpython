A=[]
i=0
j=0
k=0
counter=[]

#L=[7,18,2422]
#M=[4,93,106]
#R=[39999,99999,32399999]

#L=[1,3,10]
#M=[2,4,99]
#R=[0,8,999]

L=[3,7,9]
M=[4,5,10]
R=[2,8,11]



#L=[1,99,299]
#M=[1,1,3]
#R=[1,1,1]

print(A)

def find():
    global i
    global j
    global k
    global counter
    if i < 3:
        if j < 3 and k < 3:
            if L[i] <= M[j]:
                if L[i] <= R[k]:
                    A.append(L[i])
                    i=i+1
                    counter.append(2)
                    return
                else:
                    A.append(R[k])
                    k=k+1
                    counter.append(2)
                    return

        if j < 3 and k > 2:
            if L[i] <= M[j]:
                A.append(L[i])
                i=i+1
                counter.append(1)
                return
            else:
                A.append(M[j])
                j=j+1
                counter.append(1)
                return

        if k < 3 and j > 2:
            if L[i] <= R[k]:
                A.append(L[i])
                i=i+1
                counter.append(1)
                return
            else:
                A.append(R[k])
                k=k+1
                counter.append(1)
                return

        if i < 3 and k > 2 and j > 2:
            A.append(L[i])
            i=i+1
            counter.append(0)
            return
###################################
    if j < 3:
        if i < 3 and k < 3:
            if M[j] <= L[i]:
                if M[j] <= R[k]:
                    A.append(M[j])
                    j=j+1
                    counter.append(2)
                    return
                else:
                    A.append(R[k])
                    k=k+1
                    counter.append(2)
                    return

        if i > 2 and k < 3:
            if M[j] <= R[k]:
                A.append(M[j])
                j=j+1
                counter.append(1)
                return
            else:
                A.append(R[k])
                k=k+1
                counter.append(1)
                return                 

        if k > 2 and i < 3:
            print("trigger")
            if M[j] <= L[i]:
                A.append(M[j])
                j=j+1
                counter.append(1)
                return
            else:
                A.append(L[i])
                i=i+1
                counter.append(1)
                return                 

        if j < 3 and i > 2 and k > 2:
            A.append(M[j])
            j=j+1
            counter.append(0)
            return
###################################
    if k < 3:
        if i < 3 and j < 3:
            if R[k] <= L[i]:
                if R[k] <= M[j]:
                    A.append(R[k])
                    k=k+1
                    counter.append(2)
                    return
                else:
                    A.append(M[j])
                    j=j+1
                    counter.append(2)
                    return

        if i > 2 and j < 3:
            if R[k] <= M[j]:
                A.append(R[k])
                k=k+1
                counter.append(1)
                return
            else:
                A.append(M[j])
                j=j+1
                counter.append(1)
                return                 

        if j > 2 and i < 3:
            if R[k] <= L[i]:
                A.append(R[k])
                k=k+1
                counter.append(1)
                return
            else:
                A.append(L[i])
                i=i+1
                counter.append(1)
                return                 

        if k < 3 and i > 2 and j > 2:
            A.append(R[k])
            k=k+1
            counter.append(0)
            return
###################################


while len(A) < 9:
    find()
    print(A)
print(counter)
print(sum(counter)) 