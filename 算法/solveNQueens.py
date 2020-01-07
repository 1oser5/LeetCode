#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   solveNQueens.py
@Time    :   2020/01/05 21:31:08
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   eight-queens
'''

# here put the import lib
from typing import List
from pprint import pprint
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs(res, 0, [], [-1]*n)
        return res
    def dfs(self, res, index, path, nums):
        if len(path) == len(nums): 
            res.append(path)
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                temp = '.' * len(nums)
                self.dfs(res, index + 1, path+[temp[:i] + 'Q' + temp[i+1:]], nums)
    def valid(self, nums, n):
        for i in range(n):
            if abs(nums[i] - nums[n]) == n -i or nums[i] == nums [n]: # 列坐标相减 == 横坐标相减，表示在一对角线上，后面则判断是否为一列
                return False
        return True
if __name__ == '__main__':
    s = Solution()
    pprint(s.solveNQueens(5))
    pprint(s.solveNQueens(4))