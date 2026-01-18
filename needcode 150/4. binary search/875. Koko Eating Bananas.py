#%%
'''
I quickly realised that the solution must lie between min(piles) and max(piles)
what i failed to realise is greedy soltion will not work. and brute Force is not always a bad thing 
and we can obtimise bruth force by binary search.
the decition of bruthforce would have taken if i would have analysed the TC properly.

(USACO - guide) - from ai 
For binary search to replace brute force, the problem must exhibit monotonicity. This means if you arrange your options in order, there is a clear "tipping point" where the answer changes from "No" to "Yes."
'''

from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        extra_slot = h-len(piles)
        while extra_slot>0:
            piles.sort(reverse=True)
            for i in range(min(extra_slot, len(piles))):
                piles[i] = ceil(piles[i]/2)
            extra_slot -= lean(piles)
        
        return max(piles)
#%%
1//10
# %%
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r # one definite ans
        while l<=r:
            mid = (l+r)//2
            
            total_time = 0
            for i in piles:# we can algo reduce it to log
                total_time += ceil(i/mid)
            
            if total_time<=h:
                # we have finished up all the bananas within h hour
                # need to check if can lower it further
                r = mid-1
                k = mid
            else:
                # total time is higher than h
                # means we have choosen such a low rate, that 
                # can't finish all the bananas at time
                # need to increase the eating rate
                l = mid + 1
        
        return k

'''
1. ceil is equvalent to int_div
1//10     -> 0
ceil(..)  -> 1

2. we have to count from (1--max) not (min--max)
if h == sum(piles) 1 is valid ans 
'''