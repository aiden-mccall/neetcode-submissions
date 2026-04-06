class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = list(set(nums))

        if len(ans) != len(nums):
            return True
        else:
            return False