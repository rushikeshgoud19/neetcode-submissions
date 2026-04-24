class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h=set(nums)
        if len(h)<len(nums):
            return True
        else:
            return False
        