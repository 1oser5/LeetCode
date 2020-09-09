# -*- encoding: utf-8 -*-
'''
@File    :   solveSudoku.py
@Time    :   2020/09/09 10:20:45
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for _ in range(9)]  # 行
        col = [set(range(1, 10)) for _ in range(9)]  # 列
        block = [set(range(1, 10)) for _ in range(9)]  # 块
        empty = []  # 需要填充部分

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3) * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def dfs(index):
            # 处理完了
            if index == len(empty):
                return True
            x, y = empty[index]
            b = (x // 3) * 3 + y // 3
            # 三者交集，筛选可用元素
            for val in row[x] & col[y] & block[b]:
                row[x].remove(val)
                col[y].remove(val)
                block[b].remove(val)
                board[x][y] = str(val)
                if dfs(index + 1):
                    return True
                row[x].add(val)
                col[y].add(val)
                block[b].add(val)
            return False
        dfs(0)
if __name__ == '__main__':
    s = Solution()
    s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])