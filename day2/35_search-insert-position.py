class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for i in range(len(nums)):
            if nums[i] != target:
                if nums[i] > target:
                    return i
            else:
                return i
        return len(nums)
nums=[1,3,5,6]
target=7
p1 = Solution()
print(p1.searchInsert(nums,target))