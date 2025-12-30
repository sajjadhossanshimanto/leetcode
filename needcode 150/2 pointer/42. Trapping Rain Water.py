#%%
'''
edge case: i need at least 3 spaces to form a pocket.
- middle space may or may not be of height 0.
'''
#%%
class Solution:
    def trap(self, height: list[int]) -> int:
        
        # at least 1 ele will bee present
        water = 0
        l, r = 0, len(height)-1
        while l<r:
            if height[r] > height[l]:
                water += height[l]*(r-l)
                l = r
                r+=1
            elif height[r] < height[l]:
                ...

#%%
'''
deriving the formula:
totally depends upon observation skill. 
what is the amount of water above a bar.?
instade try asking -> why is this much water ?

water will only be trapped inside a pocket. 
and a pocket is formed if the middle bar is have higher bar on left and right.
if a higher bar is present along side of just left pos the pocket formed would be higher.
'''
class Solution:
    def trap(self, height: list[int]) -> int:
        # if len(height)<3: return 0
        
        prefix = [height[0]]
        for i in range(1, len(height)):
            prefix.append(max(prefix[-1], height[i]))
        
        suffix = [height[-1]]
        for i in range(len(height)-2, -1, -1):
            suffix.append(max(suffix[-1], height[i]))
        suffix = suffix[::-1]

        water = 0
        for i in range(1, len(height)-1):
            water += max(min(suffix[i+1], prefix[i-1])-height[i], 0)

        return water

s = Solution()
# %%
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
# %%
