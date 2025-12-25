#%%
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums.sort()
        ln = 1
        ans = ln
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1]==1:
                ln+=1
            else:
                ans = max(ln, ans)
                ln = 0
        
        return max(ans, ln)# edge 

s=Solution()
#%%
s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
# %% used number sequence to 
'''
num[i] can be 10e9. again can be negative. 
so can't actually have 2*10e9.
and the last iteration would get us time exceded.

- problem: we are westing a lot of memory here. 
- also iterating over lot of unnecessary numbers
'''
max_ln = int(10e5+7)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        num_sequence = [0]*(2*max_ln)
        for i in nums:
            num_sequence[i+max_ln] = 1
        
        ans = 0
        ln = 0
        for i in num_sequence:
            if i:
                ln+=1
            else:
                ans = max(ans, ln)
                ln = 0
        
        return max(ans, ln)

s = Solution()
# %%
s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])

# %% 45%
'''
i beleive this solution is also of nlogn
because the while loop may repeating iterations.
for 2,3,4, | 1 -> when i get 1 we are re-iterating from 1-4.

the solution can be if we cache previously seen  solution of 2
- that is disjoint set 
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        ans = 0
        nums = set(nums)
        for i in nums:
            if i-1 not in nums:
                ln = 0
                while i+ln in nums:
                    ln+=1
                ans = max(ln, ans)
        
        return ans

s = Solution()
# %%
s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])

# %%
# TODO: implement with disjoint-set.
# is disjoint set also nlogn ?