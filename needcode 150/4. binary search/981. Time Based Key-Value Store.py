#%%
class TimeMap:
    def __init__(self):
        self.time_map = {}
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[timestamp] = value
        time_list = self.keys.get(key, [])
        time_list.append(timestamp)
        self.keys[key] = time_list

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys: return ""

        time_list = self.keys[key]
        l, r = 0, len(time_list)-1
        ans = ""
        while l<=r:
            mid = (l+r)//2
            if time_list[mid]==timestamp:
                ans = self.time_map[time_list[mid]]
                break
            elif time_list[mid]<timestamp:
                ans = self.time_map[time_list[mid]]
                l = mid+1
            else:
                r = mid-1

        return ans

'''
can't return None. for None return has tobe "" empty string.
'''


s = TimeMap()
# %%
s.set('love', 'high', 10)
s.set('love', 'low', 20)
print(s.get('low', 10))
# %%
