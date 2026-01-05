#%%
from collections import deque


class Node:
    def __init__(self, key, val, next=None, previous=None):
        self.key = key
        self.val = val
        self.next = next
        self.previous = previous

class Linklist:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node

    def appendleft(self, node):
        node.next = self.head
        if not self.head:
            self.head = self.tail = node
        else:
            self.head.previous = node
            self.head = node
        

    def pop(self):
        if not self.tail:
            return 
        if self.head == self.tail:
            self.head = self.tail = None
            return
        
        key = self.tail.key
        self.tail = self.tail.previous
        self.tail.next = None
        return key

    def remove(self, node):
        # func is actually faulty. no verification either the node from the link list    
        if node.next==None and node.previous==None:# last value
            self.head = self.tail = None
        elif node.next==None:# tail
            self.tail = node.previous
            self.tail.next = None
        elif node.previous==None:# head
            self.head = node.next
            self.head.previous = None
        else: # middle of link list
            node.previous.next = node.next
            node.next.previous = node.previous


    def shift_head(self, node):
        # 1st remove the node 
        self.remove(node)
        if self.head:
            self.head.previous = node
            node.next = self.head
            node.previous = None

        self.head = node

    def __str__(self):
        arr = []
        node = self.head
        while node:
            arr.append(node.val)
            node = node.next
        
        return str(arr)

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.key_order = Linklist()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.key_order.shift_head(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity:
            pop_key = self.key_order.pop()
            self.cache.pop(pop_key)

        node = Node(key, value)
        self.cache[key] = node
        # self.key_order.append(node)
        self.key_order.appendleft(node)
        # self.key_order.shift_head(node)

obj = LRUCache(2)
#%%
# Your LRUCache object will be instantiated and called as such:
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))

"ook"
#%%
param_1 = obj.get()
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
[null,null,null,1,null,-1,null,1,-1,4]
for k, v in obj.cache.items():
    print(f"{k} -> {v.val}")
# %%
