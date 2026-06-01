def max_substring(arr, element):
    count=0
    m=0
    for i in range(len(arr)):
        if arr[i]==element:
            count+=1
            m=max(m,count)
        else: 
            count=0
    return m