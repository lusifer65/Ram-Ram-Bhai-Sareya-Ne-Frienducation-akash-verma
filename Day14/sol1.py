from sys import stdin

def sortZeroesAndOne(arr, n) :
    #Your code goes here 
    i=0
    j=0
    while(j<n):
        if(arr[j]==0):
            arr[i]=0
            i+=1
        j+=1
    
    while(i<n):
        arr[i]=1
        i+=1