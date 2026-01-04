#%%
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = type(l1)(0)
        carry = 0
        ptr = ans
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total//10

            ptr.next = ListNode(total%10)
            ptr = ptr.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            ptr.next = ListNode(l1.val+carry)
            carry = 0
            l1 = l1.next

        
        while l2:
            ptr.next = ListNode(l2.val+carry)
            carry = 0
            l2 = l2.next
        
        return ans.next
'''
issue is: 
l1 = [9,9,9,9,9,9,9] l2=[9,9,9,9]
out -> [8,9,9,9,9]
exp -> [8,9,9,9,0,0,0,1]

note: ` The digits are stored in reverse order`
'''
#%% recursion
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        def helper(l1, l2):
            if not l1.next and not l2.next:
                sum_ = l1.val + l2.val
                return type(l1)(sum_%10), sum_//10
        
            carry = 0
            if l1.next and l2.next:
                parent_node, carry = helper(l1.next, l2.next)
            elif l1.next:
                parent_node, carry = helper(l1.next, l2)
            elif l2.next:
                parent_node, carry = helper(l1, l2.next)
            
            #TODO: set the gained returned node as next of current node
            sum_ = carry + l2.val + l1.val
            node = type(l1)(sum_%10)
            parent_node.next = node
            
            return parent_node, sum_//10


        return helper(l1, l2)[0]
        
        '''
        l1 -> 9999999
        l2 -> 9999
        at one point in recursion l2[-1] but l1[-4] again l2[-1], l[-3]
        so after recusrion how do i know i don't need to sum up 
        '''

'''
another issue: 
l1 -> [2,4,3]
l2 -> [5,6,4]

out -> [8,0,7]
exp -> [7,0,8]
-- not formating the output in right order -- `corrected`
'''

#%%
def lenll(node):
    ln = 0
    while node.val:
        ln +=1
        node = node.next
    return ln

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ListNode = type(l1)

        l1_len = lenll(l1)
        l2_len = lenll(l2)

        zero_node = ListNode()
        pointer = zero_node
        for _ in range(abs(l1_len-l2_len)):
            pointer.next = ListNode(0)
            pointer = pointer.next
        zero_node = zero_node.next
        while pointer.next:
            pointer = pointer.next

        if l1_len>l2_len:
            pointer.next = l2
            l2 = zero_node
        elif l2_len>l1_len:
            pointer.next = l1
            l1 = zero_node
        # all these course just to make 2 link list in equal length!!!
        #  and now i can use the recurstion method
#%%
'''
i misunderstood the problem
what reverse order actually ment : 3456 + 789
would be given as 6 (head) -> 5 -> 4-> 3 
which actually helps !
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ListNode = type(l1)

        def adder(l1, l2, carry=0):
            v1 = l1.val
            v2 = l2.val

            total = v1+v2+carry
            l1.val = total%10
            carry = total//10
            if l1.next and l2.next:
                adder(l1.next, l2.next, carry)
            elif carry:
                if l1.next:
                    adder(l1.next, ListNode(carry), 0)
                elif l2.next:
                    l1.next = ListNode(carry)
                    adder(l1.next, l2.next, 0)
                else:
                    l1.next = ListNode(carry)
            elif l2.next:# carry is zero but l2 present
                l1.next = l2.next


        adder(l1, l2)
        return l1

s = Solution()
# %%
