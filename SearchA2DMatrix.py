class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        width = len(matrix[0])
        height = len(matrix)
        upper = 0
        lower = height - 1


        if target < matrix[0][0] or target > matrix[height - 1][width - 1]:
            return False
       
        while upper <= lower:
            mid = (upper + lower) / 2
            if target >= matrix[mid][0] and target <= matrix[mid][width - 1]: # row detected
                print(matrix[mid])
                # apply binary search on that row
                left = 0
                right = width - 1
                while left <= right:
                    mid_of_row = (left + right) / 2
                    if target == matrix[mid][mid_of_row]:
                        return True
                    elif target > matrix[mid][mid_of_row]:
                        left = mid_of_row + 1
                    else:
                        right = mid_of_row - 1
                return False
            elif target < matrix[mid][0]: # smaller than first of row
                lower = mid - 1
            elif target > matrix[mid][width - 1]: # bigger than last of row
                upper = mid + 1
        return False
