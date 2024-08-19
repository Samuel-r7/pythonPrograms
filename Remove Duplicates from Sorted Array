class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
       

        s = set(nums)
        nums.clear()
        for i in s:
           nums.append(i)
        nums.sort()
        return len(nums)
        
        #other Methods:

        # nums[:] = list(set(nums))    Does not Work
        # return len(nums)

         # j = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i-1]:
        #         nums[j] = nums[i]
        #         j +=1
        # return j
