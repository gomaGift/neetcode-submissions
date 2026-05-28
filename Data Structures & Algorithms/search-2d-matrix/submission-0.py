class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        min_row, max_row = 0, len(matrix) - 1

        while min_row <= max_row:
            mid = (min_row + max_row) // 2
            if matrix[mid][0] > target:
                max_row = mid - 1
            
            elif matrix[mid][0] < target and matrix[mid][-1] < target:
                min_row = mid + 1

            else:
                left, right = 0, len(matrix[0]) - 1
                target_arr = matrix[mid]
                while left <= right:
                    mid = (left + right) // 2
                    if target_arr[mid] == target:
                        return True
                    if target_arr[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False


        return False