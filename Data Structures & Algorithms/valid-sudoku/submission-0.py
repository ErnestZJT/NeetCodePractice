class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 使用三个集合数组分别记录每一行、每一列、每一个3x3宫格中已经出现过的数字
        # Use three arrays of sets to record digits seen in each row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]


        # 遍历整个9x9棋盘
        # Traverse the entire 9x9 board
        for r in range(9):
            for c in range(9):
                # 取出当前位置的字符
                # Get the value at the current cell
                val = board[r][c]

                # 如果当前位置是空格'.'，说明还没有填数字，直接跳过
                # If the cell contains '.', it is empty, so skip it
                if val == '.':
                    continue

                # 计算当前单元格属于哪个3x3宫格
                # Compute which 3x3 box the current cell belongs to
                box_index = (r//3)*3 + (c//3)

                # 如果该数字已经出现在当前行、当前列或当前宫格中，则数独无效
                # If the digit already exists in the current row, column, or box, the Sudoku is invalid
                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False
                
                # 否则将该数字加入对应的行集合中
                # Otherwise, add the digit to the corresponding row set
                rows[r].add(val)

                # 将该数字加入对应的列集合中
                # Add the digit to the corresponding column set
                cols[c].add(val)

                # 将该数字加入对应的3x3宫格集合中
                # Add the digit to the corresponding 3x3 box set
                boxes[box_index].add(val)

        return True


