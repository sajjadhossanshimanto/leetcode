#%%
from typing import List

def freq_counter(word:str):
    freq = {}
    for i in word:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1
    
    return tuple(freq.items())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            k = tuple(sorted(freq_counter(word)))
            if k not in anagrams:
                anagrams[k] = []
            
            anagrams[k].append(word)
        
        return list(anagrams.values())

#%%
s = Solution()
s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# %% effi solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = {}

        for word in strs:
            word_sorted = "".join(sorted(word))
            if word_sorted not in anagram_dict:
                anagram_dict[word_sorted] = []
            anagram_dict[word_sorted].append(word)
        
        return [(dict_values) for dict_values in anagram_dict.values()]