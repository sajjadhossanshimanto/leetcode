#%% 100% effi
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> List[int]:
        c = Counter(nums)
        # return sorted(c.items(), key=lambda x:x[1])
        return list(map(lambda x: x[0], sorted(tuple(c.items()), key=lambda x:x[1])[-k:]))

s = Solution()
#%%
s.topKFrequent( nums = [1,1,1,2,2,3], k = 2)
# %%
