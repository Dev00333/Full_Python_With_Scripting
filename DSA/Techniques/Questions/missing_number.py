def missing_num(arr):
    l=len(arr)
    boo=[False]*(l+1)
    for i in range(l):
        boo[arr[i]]=True
    for i in range(len(boo)):
        if boo[i]==False: return i
    return "All Present"