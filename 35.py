# 暴力法
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums==None or len(nums)==0:
            return 0
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)



# 二分法
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l if nums[l] >= target else l + 1
