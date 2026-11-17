class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        flag=True
        for i in range(len(nums)):
            if nums[i]==target:
                flag=False
                return i
        if flag:
            nums.append(target)
            nums.sort()
            for j in range(len(nums)):
                if nums[j]==target:
                    return j
            