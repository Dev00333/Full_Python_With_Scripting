def trail(arr):
    l=len(arr)
    if l<=1: return arr
    i=0
    j=l-1
    while i<j :
        if arr[i]==0 and arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        elif arr[i]==0 and arr[j]==0:
            j-=1
        else:
            i+=1
    return arr

def trail_pos(arr):
    l=len(arr)
    pos=0
    for i in range(l):
        if arr[i]!=0:
            arr[pos]=arr[i]
            pos+=1
    arr[pos:]=[0]*(l-pos)