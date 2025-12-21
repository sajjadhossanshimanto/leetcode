'''
https://leetcode.com/problems/product-of-array-except-self/description/

- target need to calculate product in O(n)
'''
#%% 99% memory and process
from typing import List



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = None
        zero_count = 0
        ans = []

        for i in nums:
            if i==0: 
                zero_count += 1
                continue 
            if total is None:
                total = i
            total *= i
    
        for i in nums:
            if i==0:
                ans.append(0 if zero_count-1 else total)
            else:
                ans.append(0 if zero_count else total/i)

        return ans

s = Solution()
#%% wa case
s.productExceptSelf([0, 0])
# out -> [1, 1]
# exp -> [0, 0]
# %% 
'''
the most cummon solution uses prefix and suffix array to solve. 
----> good to learn the use of sufix array and their combination 
- for the solution we need continious multiplication of numbers befor it --> prefix array 
- not only behind numbers we also need product of number after --> suffix array 
- solution at any point is `prefix[i-1]*sufix[i+1]` eleminating the `i`- th number


'''
