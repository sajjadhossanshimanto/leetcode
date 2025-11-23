#%%
# can be solved mathematically 
# or using string
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        new_num = 0
        n_sum = 0
        digit_count = 0
        
        while n:
            last_digit = n%10
            n = n//10
            if last_digit!=0:
                new_num = new_num+last_digit*(10**digit_count)
                n_sum += last_digit
                digit_count+=1

        return new_num*n_sum

#%%
s = Solution()
s.sumAndMultiply(10203004)

# %%
s.sumAndMultiply(1000)
# %%
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n = str(n)
        n = n.replace('0', '')
        # edge1: now as n is string.. string can be empty.
        # python int can't accept empty string.
        if not n: return 0

        return sum(map(int, n))*int(n)

# %%
