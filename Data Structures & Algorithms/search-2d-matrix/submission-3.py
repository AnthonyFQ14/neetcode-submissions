class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == target:
        #             return True

        lRow = 0
        rRow = len(matrix) - 1

        for i in range(len(matrix)):
            
            if matrix[i][len(matrix[i]) - 1] < target:
                print("continuing")
                continue

            l = 0
            r = len(matrix[i]) - 1

            while l <= r:
                mid = (l + r) // 2

                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    l = mid + 1
                elif matrix[i][mid] > target:
                    r = mid - 1
            

        return False