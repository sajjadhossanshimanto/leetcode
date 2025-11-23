#%%
mod = 1e9+7
class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        nums_count = [s[0]]
        pre_sum = [int(s[0])]
        
        for i in s[1:]:
            if i=='0': 
                nums_count.append(nums_count[-1])
                pre_sum.append(pre_sum[-1])
                continue
            
            nums_count.append(nums_count[-1]+i)
            pre_sum.append(pre_sum[-1]+int(i))

        # print(nums_count)
        # print(pre_sum)

        ans = []
        for l, r in queries:
            if l==0:
                ans.append(int((int(nums_count[r])*pre_sum[r])%mod))
                continue
            
            num = nums_count[r][len(nums_count[l-1]):]
            if not num:
                ans.append(0)
            else:
                num = int(num)# edge: int(empty_str)©leetcode
                s = pre_sum[r]-pre_sum[l-1]
                ans.append(int((int(num)*s)%mod))
        
        return ans
# %%
s = Solution()
s.sumAndMultiply(s = "10203004", queries = [[0,7],[1,3],[4,6]])
# %%
s.sumAndMultiply("9876543210", [[0,9]])
# %%
