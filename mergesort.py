#Program for MergeSort

def mergesort(array):
    if len(array)>1:
        M=len(array)//2                 #Midpoint of array
        L=array[:M]                     #Left half of array        
        R=array[M:]                     #Right half of array
        
        mergesort(L)                    #Mergesort for Left array
        mergesort(R)                    #Mergesort for Right array
    
        a=0
        b=0
        c=0

        while a<len(L) and b<len(R):    
            if L[a]<R[b]:               #Checking for smallest value in both arrays 
                array[c]=L[a]           #and adding smallest to array
                a+=1
            else:
                array[c]=R[b]
                b+=1
            c+=1
        while a<len(L):                 #Adding rest of the values from left array after right is empty
            array[c]=L[a]
            a+=1
            c+=1
        while b<len(R):                 #Adding rest of the values from right array after left is empty
            array[c]=R[b]
            b+=1
            c+=1

#Main component 
A=list(map(int,input("Enter elements of list: ").split()))      #Taking input from the user
mergesort(A)                                            
print("List after sorting: ",end="")
for i in range(len(A)):
    print(str(A[i]),end=" ")
                
