#%%
def key(x):
    return (int(bin(x)[2:][::-1]), x)

class Solution:
    def sortByReflection(self, nums: list[int]) -> list[int]:
        return list(sorted(nums, key=key))


# %%
