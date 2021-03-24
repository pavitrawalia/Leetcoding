class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float("-inf")
        tempSum = 0
        for i in range(len(nums)):
            tempSum += nums[i]
            result = max(result, tempSum)
            if tempSum < 0:
                tempSum = 0
        return result
