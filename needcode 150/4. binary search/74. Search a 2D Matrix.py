
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l<=r:# choose the row
            mid = (l+r)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif matrix[mid][0]>target:
                # eleminate right half
                r = mid-1
            else:
                l = mid+1
        else:
            return False
        
        arr = matrix[mid]
        l, r = 0, len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid]==target:
                return True
            elif arr[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return False
        