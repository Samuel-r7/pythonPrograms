class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curSum = 0

        curSum = sum(nums[:k])
        max_avg = curSum

        for i in range(k,n):
            curSum += nums[i] - nums[i-k]
            max_avg = max(max_avg,curSum)
        
        return max_avg / k
        
