#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   kthSmallest.py
@Time    :   2020/07/02 08:57:10
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        size = len(matrix)

        def check(mid):
            i, j = size - 1, 0
            num = 0
            while i >= 0 and j < size:
                # If current num smaller than mid, means there is i + 1 num smaller than mid
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    pass