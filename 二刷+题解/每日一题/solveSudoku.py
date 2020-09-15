class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    cur = int(board[i][j])
                    b = (i // 3) * 3 + j // 3
                    # remove already exists number
                    row[i].remove(cur)
                    col[j].remove(cur)
                    block[b].remove(cur)
                else:
                    empty.append((i, j))

        def dfs(index):
            if index == len(empty):
                return True
            x, y = empty[index]
            b = (x // 3) * 3 + y // 3
            for res in row[x] & col[y] & block[b]:
                row[x].remove(res)
                col[y].remove(res)
                block[b].remove(res)
                board[x][y] = str(res)
                if dfs(index + 1):
                    return True
                row[x].add(res)
                col[y].add(res)
                block[b].add(res)
            return False
        dfs(0)



