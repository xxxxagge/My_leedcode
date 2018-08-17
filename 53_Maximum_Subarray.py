# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        count = maxsum = nums[0]
        for i in nums[1:]:
        	count = max(i,i+count)
        	maxsum = max(maxsum,count)
        return maxsum
s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))

        