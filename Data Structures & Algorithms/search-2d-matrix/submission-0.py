class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in matrix:
            for y in x:
                if y ==target:
                    return True
        return False
        