#%% bruth force
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target: 
                    return i, j

#%% O(n)
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i in range(len(nums)):
            sum_dict[nums[i]] = i
        
        for j in range(len(nums)):
            left = target-nums[j]# can't use same number mulltiple time
            if left in sum_dict and sum_dict[left]!=j:
                return sum_dict[left], j

s = Solution()
print(s.twoSum(nums = [3,2,4], target = 6))
# %%
