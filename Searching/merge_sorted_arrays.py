def mrege_2_sorted_arrays(one,two):
    m=len(one)
    n=len(two)
    c=[0]*(m+n)
    i=j=k=0
    if m>0 and n>0:
        c[k]=min(one[i], two[j])
        k+=1
    while i<m and j<n:
        if one[i]<two[j]:
            if one[i]==c[k-1]:
                i+=1
                continue
            c[k]=one[i]
            i+=1
            k+=1
        elif one[i]>two[j]:
            if two[j]==c[k-1]:
                j+=1
                continue
            c[k]=two[j]
            j+=1
            k+=1
        elif one[i]==two[j]:
            if one[i]==c[k-1]:
                i+=1
                j+=1
                continue
            c[k]=one[i]
            i+=1
            j+=1
            k+=1
    if i==m:
        for x in range(j,n):
            if two[x]==c[k-1]:
                continue
            c[k]=two[x]
            k+=1
    elif j==n:
        for x in range(i,m):
            if one[x]==c[k-1]:
                continue
            c[k]=one[x]
            k+=1
    return c[:k]