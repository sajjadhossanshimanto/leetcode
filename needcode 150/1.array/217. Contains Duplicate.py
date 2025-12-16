class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return bool(len(nums)-len(set(nums)))