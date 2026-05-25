class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        starters = [i[0] for i in matrix]
        l,r = 0 ,len(starters)-1
        while l<=r:
            mid = l+(r-l)//2
            if starters[mid]==target:
                return True
            elif starters[mid]<target:
                l = mid+1
            else:
                r = mid-1
        row = matrix[l-1]
        l,r = 0,len(row)-1
        while l<=r:
            mid = l+(r-l)//2
            if row[mid]==target:
                return True
            elif row[mid]<target:
                l=mid+1
            else:
                r = mid-1
        return False