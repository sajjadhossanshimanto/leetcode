#%% solves in o(n)
'''
alpha numeric includes -> alphabers and number.

'''

def filter_alap(s: str):
    s = s.lower()
    l = []
    for i in s:
        if (ord(i)>=97 and ord(i)<=122) or (48<=ord(i)<=57):
            l.append(i)
    
    return "".join(l)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = filter_alap(s.lower())
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
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = filter_alap(s)
        # we could have applied that same fillter while iteration for palindrom match
        

        l, r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False

            l+=1
            r-=1
        
        return True
