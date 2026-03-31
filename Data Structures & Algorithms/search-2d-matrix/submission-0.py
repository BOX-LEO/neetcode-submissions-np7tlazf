class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c0,c1 = 0,len(matrix)-1
        while c0+1<c1:
            mid = int((c1-c0)/2)+c0
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]>target:
                c1 = mid
            else:
                c0=mid
        if matrix[c1][0]>target:
            c = c0
        else:
            c = c1
        row = matrix[c]
        l,r = 0,len(row)-1
        while l+1<r:
            mid = l+int((r-l)/2)
            if row[mid]==target:
                return True
            elif row[mid]<target:
                l=mid
            else:
                r = mid
        if row[l]==target or row[r]==target:
            return True
        return False
        