def right_rot_k_place(arr,k):
    l=len(arr)
    if l<2: return arr
    rot=k%l
    return arr[-rot:]+arr[:-rot]

# def in_place_rot(arr,k):
#     l=len(arr)
#     if l<2: return arr
#     rot=k%l
#     count=0
#     nums = []*rot
#     for i in range(rot):
#         nums[i]=arr[rot+i]
#     for i in range(rot, l):
#         arr[i]=arr[count]
#         count+=1
#     for i in range(rot):
#         arr[i]=