def two_sum(arr, target):
    for i in range(len(arr)):
        temp1=target-arr[i]
        for j in range(i+1,len(arr)):
            temp2=temp1-arr[j]
            if temp2==0: return [i,j]
    return [-1,-1]

def two_sum_optimised(arr, target):
    seen={}
    for i in range(len(arr)):
        current_num=arr[i]
        needed=target-current_num