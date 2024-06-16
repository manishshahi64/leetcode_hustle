class Solution:  
    def removeDuplicates(self, nums) -> int:
        k = 1       
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                print(nums[k],nums[i])
                nums[k] = nums[i]
                k+=1
        return k
nums = [1,1,2,2,2,2,4,7]
p1 = Solution()
print(p1.removeDuplicates(nums))