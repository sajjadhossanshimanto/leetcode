'''
https://leetcode.com/problems/merge-two-sorted-lists/description/
'''
#%%
from typing import Optional
from heapq import heappush, heappop


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        index = []
        while list1 or list2:
            if list1:
                heappush(index, list1.val)
                list1 = list1.next
            if list2:
                heappush(index, list2.val)
                list2 = list2.next
        
        if not index:
            return None
        
        head = ListNode(heappop(index))
        node = head
        while index:
            node.next = ListNode(heappop(index))
            node = node.next

        return head

#%%
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # cummon edge case
        if not list1 and not list2: return 
        if list2 and not list1: return list2
        if list1 and not list2: return list1

        link_list = type(list1)

        ans = link_list()
        ptr = ans
        while list1:
            while list2 and list1.val >= list2.val:
                ptr.next = list2
                list2 = list2.next
                ptr = ptr.next
                ptr.next = None
            
            ptr.next = list1
            list1 = list1.next
            ptr = ptr.next
            ptr.next = None

        # so far we only have added numbers that are less or edual to list1 
        # list2 might left with larger numbers 
        if list2:# important edge
            ptr.next = list2

        return ans.next


s = Solution()
# %%
from link_helper import list_to_link, print_link

l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
l1=[]
l2=[]
# %%
ans = s.mergeTwoLists(list_to_link(l1), list_to_link(l2))
print_link(ans)

# %%
