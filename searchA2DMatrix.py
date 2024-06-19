class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        begRow, endRow = 0, len(matrix)-1

        while begRow <= endRow:
            midRow = (begRow+endRow) // 2

            if target in matrix[midRow]:
                return True
            
            if target < matrix[midRow][0]:
                endRow = midRow-1
            else:
                begRow = midRow+1

        return False