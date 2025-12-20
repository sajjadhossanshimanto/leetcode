'''
https://leetcode.com/problems/product-of-array-except-self/description/

- target need to calculate product in O(n)
'''
#%% wa
from typing import List



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        ans = []
        if 0 in nums:
            for i in nums:
                if i==0: continue 
                total *= i
        
            for i in nums:
                if i==0:
                    ans.append(total)
                else:
                    ans.append(0)
        else:
            for i in nums:
                total *= i
            
            for i in nums:
                ans.append(total//i)
        
        return ans

s = Solution()
#%% wa case
s.productExceptSelf([0, 0])
# out -> [1, 1]
# exp -> [0, 0]