class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return False
        col_start = [i[0] for i in matrix]
        t,b = 0,len(col_start)-1
        while t<=b:
            mid = t+(b-t)//2
            if col_start[mid]==target:
                return True
            if col_start[mid] > target:
                b-=1
            else:
                t+=1
        target_row = t-1
        row = matrix[target_row]
        l,r = 0, len(row)-1
        while l<=r:
            mid = l+(r-l)//2
            if row[mid] == target:
                return True
            elif row[mid]>target:
                r=mid-1
            else:
                l = mid+1
        return False
