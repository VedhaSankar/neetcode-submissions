class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # solution 2 (better)

        nums_hashmap = {}

        for i, j in enumerate (nums):
            if ((target - j) in nums_hashmap):
                return [nums_hashmap.get(target - j), i]
            else:
                nums_hashmap[j] = i


        # solution 1
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             return [i, j]
                


