from collections import Counter

class Solution:
    def countElements(self, nums: list[int], k: int) -> int:
        nums = Counter(nums)
        
        for i in sorted(nums.keys()):

        