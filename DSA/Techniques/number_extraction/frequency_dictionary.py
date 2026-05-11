# in pythin it is known as frequency dictionary
# in other languages it is known as hash map or hash table
nums=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,8,4,2,1,8,9,0,3,2,2,2]

def frequency_dictionary(nums):
    freq_map={}
    for i in nums:
        if i in freq_map:
            freq_map[i]+=1
        else:
            freq_map[i]=1
    return freq_map
print(frequency_dictionary(nums))

# the time complexity is O(n)
# the space complexity is O(n)
# above complexities are of worst case only

# meathod 2 using hashing

def hashmap_using_function(nums):
    n=len(nums)
    hash_map={}
    for i in range(0,n):
        hash_map[nums[i]]=hash_map.get(nums[i],0)+1
    print(hash_map)

hashmap_using_function(nums)

# the time complexity now is O(n) in worst case scenario
# but in case when input are not having repeating values the time complexity is O(1)