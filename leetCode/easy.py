def twoSum(nums, target):
    dict={}
    for k,v in enumerate(nums):
        result=target-v
        if result in dict:
            print([dict[result], k])
        dict[v] = k
twoSum([9, 0, 2, 11, 7, 15], 9)