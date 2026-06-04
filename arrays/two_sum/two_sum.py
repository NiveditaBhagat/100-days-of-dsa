class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_nums={}

        for index, value in enumerate(nums):
            num1=target-value
            if num1 in seen_nums:
                return [seen_nums[num1],index]
            seen_nums[value]=index
