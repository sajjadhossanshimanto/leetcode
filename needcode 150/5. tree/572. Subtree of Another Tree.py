# %%
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not root: return False# is empty tree is considered as sub-tree?
        
        # if root.val == subRoot.val:
            # return self.is_sametree(root, subRoot)
            # edge : dublicate value allowed 
        if self.is_sametree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_sametree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        
        return self.is_sametree(p.left, q.left) and self.is_sametree(p.right, q.right)

s= Solution()
#%%
# from tree_helper import etu_to_tree, process_tree, draw_graph
s.isSubtree(
    etu_to_tree([3,4,5,1,None,2]),
    etu_to_tree([3, 1, 2])
)
# 3 is equ to 3
# then is 1 sub-tree : yes
# is 2 sub-tree : yes
# but the thing is it is not attached. 
# sub-tree and same tree is not the same concept
# this question reqired to match same tree
# %%
