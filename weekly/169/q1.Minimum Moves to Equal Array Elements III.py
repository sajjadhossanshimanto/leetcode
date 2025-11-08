# https://leetcode.com/contest/biweekly-contest-169/problems/minimum-moves-to-equal-array-elements-iii/description/
# easy question

#%%
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        avg = max(nums)
        cost = 0
        for i in nums:
            cost += abs(avg-i)
        return avg

s=Solution()
# %%
