# Approach 1
class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums



# Approach 2: Using a New Array (Beginner Friendly)

class Solution(object):
    def runningSum(self, nums):
        result = []
        curr_sum = 0

        for num in nums:
            curr_sum += num
            result.append(curr_sum)

        return result
