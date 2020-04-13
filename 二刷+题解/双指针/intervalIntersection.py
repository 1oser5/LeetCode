#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   intervalIntersection.py
@Time    :   2020/04/13 16:59:10
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定两个由一些闭区间组成的列表，每个区间列表都是成对不相交的，并且已经排序。

返回这两个区间列表的交集。

（形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b。两个闭区间的交集是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/interval-list-intersections
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        index_a = 0
        index_b = 0
        while index_a < len(A) and index_b < len(B):
            low = max(A[index_a][0], B[index_b][0])
            high = min(A[index_a][1], B[index_b][1])
            if low <= high:
                res.append([low, high])
            if A[index_a][1] < B[index_b][1]:
                index_a += 1
            else:
                index_b += 1
        return res

if __name__ == '__main__':
    s = Solution()
    #c = s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]])
    c = s.intervalIntersection([[5,10]], [[3,10]])
    print(c)