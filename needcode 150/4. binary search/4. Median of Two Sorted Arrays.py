#%%
class Solution:
    def single_median(self, nums):
        n = len(nums)
        if n&1==1:
            return nums[n//2]
        
        return (nums[n//2]+nums[n//2-1])/2

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n<m:
            n, m = m, n
            nums1, nums2 = nums2, nums1
        
        if n==0 or m==0:
            return self.single_median(nums1 or nums2)


        if (n+m)&1==1:
            median_index = (m+n)//2
            l, r = 0, len(nums1)-1
            mid = (l+r)//2
            mid2 = median_index - (mid+1)
            # return nums1[mid], nums2[mid2]# mid point test
            while mid+1<n and not nums1[mid+1] >= nums2[mid2]:
                mid2-=1
            """
            It's ok to reduce 1 by 1 but as the array is sorted 
            and we are eventually finding a number that is less than a fix number 
            why not use binary search.
            """
            
            while mid2+1<m and not nums1[mid] >= nums2[mid2+1]:
                mid-=1
            
            return max(nums1[mid], nums2[mid2])
        else:
            median_index = (m+n)//2
            l, r = 0, len(nums1)-1
            mid = (l+r)//2
            mid2 = median_index - (mid+1) -1
            while mid+1<n and not nums1[mid+1] >= nums2[mid2]:
                mid2-=1
            
            while mid2+1<m and not nums1[mid] >= nums2[mid2+1]:
                mid-=1

            if mid+1 < n and mid2+1 < m:
                return (max(nums1[mid], nums2[mid2]) + min(nums1[mid+1], nums2[mid2+1]))/2
            elif mid+1<n:
                return (max(nums1[mid], nums2[mid2]) + min(nums1[mid+1], nums2[mid2]))/2
            elif mid2+1<m:
                return (max(nums1[mid], nums2[mid2]) + min(nums1[mid], nums2[mid2+1]))/2
            return (max(nums1[mid], nums2[mid2]) + min(nums1[mid], nums2[mid2]))/2


s = Solution()
# %%
s.findMedianSortedArrays(
    list(range(8)),
    list(range(5))
)
#%%
s.findMedianSortedArrays(
    [1, 3],
    [2]
)
#%%
s.findMedianSortedArrays(
    [1,2],
    [3,4]
)
# %%
s.single_median(
    # list(range(1, 7))
    []
)
# %%
"""
given 
- have to solve in logarithmic TC
- and the array is sorted

these clearly indicates binary search. (probably)
the 1st hit point should be `binary search`
if not work we can look for other
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        if len(A)>len(B):
            A, B = B, A
        n, m = len(A), len(B)
        
        l, r = 0, n-1
        half = (n+m)//2
        while l<=r:
            i = (l+r)//2
            j = half - i -2
            # (half - (aleft + 1)) - 1

            l1 = A[i] if i>=0 else float("-infinity")
            r1 = A[i+1] if i+1<n else float("infinity")
            l2 = B[j] if j>=0 else float("-infinity")
            r2 = B[j+1] if j+1<m else float("infinity")

            if l1 <= r2 and l2 <= r1:
                if (n+m)&1:
                    return (max(l1, l2) + min(r1, r2)) / 2

                return min(r1, r2)
            elif l1 > r2:
                r = i-1
            else: 
                l = r+1


#%%
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1