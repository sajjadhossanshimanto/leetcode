#%%
'''
in 2 pointer we can sum 2 nums 
in 3 sum we can iterate over each number and then apply 2 sum algo 
making it O(n^2).
there is no way to reduce any further. 

issue: is ans can't contain any dublicate . to avoid dublicates
1. while adding to the ans list. watch for if already added. 
- that is using a set to store ans for effitient lookup
- again we can't store unhashable `list` inside `set`
- also we need to sort before adding to ans 
- this actually a horrible solution

2. sort the initial array before iterate.
- avoid iterating the same number. when nums[i]==nums[i-1]
'''
#%%
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sum_dict = {}
        for i in range(len(nums)):
            sum_dict[nums[i]] = i
        
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                ele = nums[i] + nums[j] 
                if -ele in sum_dict:
                    # ans.append()
                    # ans.add(tuple(sorted([i, j, sum_dict[-ele]])))
                    ans.add(tuple(sorted([nums[i], nums[j], -ele])))
        return list(ans)
#%%
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted((nums))

        sum_dict = {}
        for i in range(len(nums)):
            sum_dict[nums[i]] = i
        print(sum_dict)

        ans = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: continue
            for j in range(i+1, len(nums)):
                if j-1>i and nums[j-1]==nums[j]: continue
                ele = -(nums[i]+nums[j])
                if ele in sum_dict and sum_dict[ele]>j:
                    ans.append([nums[i], nums[j], ele])
                    # sum_dict.pop(ele)# ensure no dublicates# poping the element will break the algo 
                # for k in range(j+1, len(nums)):
                    # if nums[i]+nums[j]+nums[k] == 0:
                    # ans.append([nums[i], nums[j], nums[k]])
        return ans

s = Solution()
# %%
s.threeSum(nums = [-1,0,1,2,-1,-4])
# [[-1,-1,2],[-1,0,1]] 
# %%
# TODO: not solved yet
s.threeSum([0, 0, 0])
# %%
