class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix = [[0]]
            return
        rows, cols = len(matrix), len(matrix[0])
        # 创建大小为 (rows + 1) x (cols + 1) 的前缀和矩阵，多出的一行一列用于简化边界计算
        self.prefix = [[0] * (cols + 1) for _ in range(rows+1)]

        # 遍历原矩阵，构建二维前缀和
        # Traverse the original matrix and build the 2D prefix sum
        for r in range(rows):
            for c in range(cols):
                # 当前前缀和 = 上方前缀和 + 左侧前缀和 - 左上角重复部分 + 当前元素值
                # Current prefix sum = top + left - top-left overlap + current matrix value
                self.prefix[r+1][c+1] = (
                    self.prefix[r][c+1] + 
                    self.prefix[r+1][c] -
                    self.prefix[r][c] + 
                    matrix[r][c]
                )
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = (self.prefix[row2+1][col2+1] - 
        # 减去上方多余区域
        # Subtract the extra upper area
        self.prefix[row1][col2+1] - 
        # 减去左侧多余区域
        # Subtract the extra left area
        self.prefix[row2+1][col1] + 
        # 加回被重复减去的左上角区域
        # Add back the top-left area that was subtracted twice
        self.prefix[row1][col1])
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)