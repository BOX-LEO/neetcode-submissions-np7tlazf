class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,columns = len(matrix),len(matrix[0])
        l,r = 0, rows*columns-1
        while l<=r:
            mid = l+(r-l)//2
            x,y = mid//columns, mid%columns
            temp = matrix[x][y]
            if temp == target:
                return True
            elif temp<target:
                l=mid+1
            else:
                r = mid-1
        return False