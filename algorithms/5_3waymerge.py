i=0
j=0
k=0

xValid=False
A=[None]*9

#L=[7,8,9,9999]
#M=[4,5,6,9999]
#R=[1,2,10,9999]

#L=[0,8,999,9999999]
#M=[3,9,12222,9999999]
#R=[72,85,10,9999999]


L=[7,18,2422]
M=[4,93,106]
R=[3,99,323]
'''
L=[1,2,3]
M=[4,5,6]
R=[7,8,9]
'''
print(A)
'''
for q in range(0,9):
    if(not xValid):
        if(k < 3 and j < 3):
            if(M[j]<=R[k]):
                x=M[j]
                j=j+1
            else:
                x=R[k]
                k=k+1
            xValid=True
        else:
                if(k<3):
                    x=R[k]
                    k=k+1
                else:
                    if(j<3):
                        x=M[j]
                        j=j+1
        xValid=True
    if (i<3):
        if(k < 3 or j < 3):
            if(L[i]<= x):
                A[q]=L[i]
                i=i+1
                xValid=False
            else:
                A[q]=x
                xValid=False
        if(k>2 and j>2):
            A[q]=L[i]
            i=i+1  
        else:
            A[q]=x
            xValid=False
print(A)
'''


'''
for q in range(0,9):
    if(not xValid):
        if(M[j]<=R[k]):
            x=M[j]
            j=j+1
        else:
            x=R[k]
            k=k+1
        xValid=True
    if (L[i]<= x):
        A[q]=L[i]
        i=i+1
    else:
        A[q]=x
        xValid=False
print(A)
'''

for q in range(0,9):
    if(i < 3 and j < 3 and k < 3):
        if(M[j]<=R[k]):
           if(M[j]<=L[i]):
               A[q]=M[j]
               j=j+1

        if(M[j]<=L[i]):
           if(M[j]<=R[k]):
               A[q]=M[j]
               j=j+1

        if(R[k]<=M[j]):
           if(R[k]<=L[i]):
               A[q]=R[k]
               k=k+1 

        if(R[k]<=L[i]):
           if(R[k]<=M[j]):
               A[q]=R[k]
               k=k+1

        if(L[i]<=M[j]):
           if(L[i]<=R[k]):
               A[q]=L[i]
               i=i+1
               
        if(L[i]<=R[k]):
           if(L[i]<=M[j]):
               A[q]=L[i]
               i=i+1 
        
        '''
        if(not xValid):
            if(M[j]<=R[k]):
                x=M[j]
                j=j+1
            else:
                x=R[k]
                k=k+1
            xValid=True
        if (L[i]<= x):
            A[q]=L[i]
            i=i+1
        else:
            A[q]=x
            xValid=False
        '''
    if( i < 3 and j < 3 and k > 2 ):
        if(L[i]<M[j]):
            A[q+1]=L[i]
            i=i+1
        else:
            A[q+1]=M[j]
            j=j+1

    if( i < 3 and k < 3 and j > 2):
        if(L[i]<R[k]):
            A[q+1]=L[i]
            i=i+1
        else:
            A[q+1]=R[k]
            k=k+1
    
    if( j < 3 and k < 3 and i > 2):
        if(M[j]<R[k]):
            A[q+1]=M[j]
            j=j+1
        else:
            A[q+1]=R[k]
            k=k+1
    
    if(i<3 and j>2 and k>2):
        A[q+2]=L[i]
        i=i+1
    
    if(j<3 and i>2 and k>2):
        A[q+2]=M[j]
        j=j+1

    if(k<3 and i>2 and j>2):
        A[q+2]=R[k]
        k=k+1


print(A)