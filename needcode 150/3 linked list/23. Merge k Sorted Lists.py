#%% trash solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists: return 
        if len(lists)==1: return lists[0]

        ListNode = type(lists[0])
        merged = ListNode()
        pointer = merged
        while any(lists):
            lists = sorted(lists, key=lambda x:x.val if x else 0)
            for i in range(len(lists)):
                if isinstance(i, int): continue
                j = i+1
                if j==len(lists): j=0
                while lists[i].val<=lists[j].val:
                    # add the i'th node to merged list
                    node = lists[i]
                    lists[i] = node.next
                    node.next = None

                    pointer.next = node
                    pointer = node
            
        return merged.next

# %%
"""
merge sort devide and conquer technique
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if len(lists)==1: return lists

        mid = len(lists)//2
        l1 = self.mergeKLists(lists[:mid])
        l2 = self.mergeKLists(lists[mid:])

        ans = type(l1)()
        pointer = ans
        while l1:# iterating over l1
            while l2 and l1.val>l2.val:
                pointer.next = l2
                l2 = l2.next
                pointer = pointer.next
                pointer.next = None
            
            pointer = l1
            l1 = l1.next
            pointer = pointer.next
            pointer.next = None
        
        if l2:
            pointer.next = l2

        return ans.next