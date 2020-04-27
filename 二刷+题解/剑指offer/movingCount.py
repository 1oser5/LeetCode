#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   movingCount.py
@Time    :   2020/04/26 15:30:49
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        res = 0
        stack = [(0, 0)]
        memory = set()
        while stack:
            x, y = stack.pop(0)
            count = self.count(x, y)
            if count > k or (x, y) in memory:
                continue
            res += 1
            memory.add((x, y))
            if x < m-1:
                stack.append((x+1, y))
            if y < n-1:
                stack.append((x, y+1))
        return res

    def count(self, x, y):
        s = 0
        str_x = str(x)
        str_y = str(y)
        for i in str_x:
            s += int(i)
        for j in str_y:
            s += int(j)
        return s

if __name__ == '__main__':
    s = Solution()
    c = s.movingCount(3, 2, 1)
    print(c)