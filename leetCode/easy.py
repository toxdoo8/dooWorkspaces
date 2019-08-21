def twoSum(self, nums, target):
        dict={}
        for k,v in enumerate(nums):
            result=target-v
            if result in dict:
                return [dict[result], k]
            dict[v]=k


