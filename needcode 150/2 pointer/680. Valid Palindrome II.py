'''
palindrom manei 2 pointer
'''
#%%
class Solution:
    def validPalindrome(self, s: str) -> bool:
        mismatch_count = 0
        l, r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                # print(l, r)
                if mismatch_count: 
                    return False
                mismatch_count += 1
                
                '''
                greedy approach is not working.
                    l -> a[bc]ef
                    r -> a[cb]cef
                    both [l+1]==[r] and [r-1]==[l]
                by looking we need remove `c` to make it palindrom
                but out implementation priorities removing the left char first
                '''
                if s[l+1] == s[r]: # removing left char
                    l+=1
                elif s[r-1]==s[l]:
                    r-=1
                else: 
                    return False # this should be reached
            else:
                l+=1
                r-=1
        
        return True

s = Solution()
# %%
s.validPalindrome("abca")
# %%
s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")
# %%
def is_palindrom(l, r, s):
    while l<r:
        if s[l]!=s[r]: return False
        l+=1
        r-=1

    return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return is_palindrom(l+1, r, s) or is_palindrom(l, r-1, s)

            l+=1
            r-=1
        
        return True
