#%% 
# my solution is not optimising the property: given array is sorted
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(numbers)):
            # if numbers[i] > target: break # condition will fail if the target is negative
            # target = -5,  [-2, 7] -> as 7>target 7 will never be touched
            cache[numbers[i]] = i

        for i in range(len(numbers)):
            j = target-numbers[i]
            if j in cache and cache[j]!=i:
                return (sorted([i+1, cache[j]+1])) # 1 - indexing

s = Solution()

# %%
s.twoSum(numbers = [2,7,11,15], target = 9)
#%%
s.twoSum([-1,-1,1,1,1,1,1,1], -2)
# %% most effitient
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers) - 1

        while l<r:
            if numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                return [l+1, r+1]
