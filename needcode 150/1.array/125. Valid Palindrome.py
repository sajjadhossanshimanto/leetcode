#%% solves in o(n)
'''
alpha numeric includes -> alphabers and number.

'''

def filter_alap(s):
    for i in s:
        if (ord(i)>=97 and ord(i)<=122) or (48<=ord(i)<=57):
            yield i

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(list(filter_alap(s.lower())))
        return s==s[::-1]
        return s

s = Solution()
#%%
s.isPalindrome("A man, a plan, a canal: Panama")
# %%
s.isPalindrome("0p")
# %%
ord("9")
# %%
# TODO: solve in O(logn) with 2 pointer