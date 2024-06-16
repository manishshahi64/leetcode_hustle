class Solution:
    def removeElement(self, nums, val: int) -> int:
        output = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[output] = nums[i]
                output +=1
        return output
nums =[0,1,2,2,3,0,4,2]
val = 2
p1 = Solution()
print(p1.removeElement(nums,val))