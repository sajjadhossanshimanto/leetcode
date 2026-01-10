'''
- `can't modify the array` -> can't sort it
- `in O(1) space` -> can't create set or link list or disjoint set

i can just traverse the array and need to tell the repeated ans.

max ln -> 10^5 so expectected TC: O(n) or O(nlogn)
tag: you can't solve if you haven't seen before. 

create a linklist or graph if a number is repeated there will be a cycle. 
- to ditect cycle use : floyd's turtle and hare
- for the constant storage : we will consider ll in array format
    - where numbers and position will work as pointer and value 
    - this only works because the value is `int`

TODO: what are all the problem and use case of link list loop detection
'''
#%%
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # provided: len will not be 1 or 0
        if len(nums)==2: return nums[0]

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break 
        
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow==fast:
                return slow