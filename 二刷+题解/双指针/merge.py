#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   merge.py
@Time    :   2020/04/13 18:55:57
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        stack = []
        for val in intervals:
            if stack:
                if stack[-1][1] >= val[0]:
                    low, high = stack.pop()
                    stack.append([low, max(high, val[1])])
                    continue
            stack.append(val)
        return stack

if __name__ == '__main__':
    s = Solution()
    c = s.merge([[1,3],[2,6],[8,10],[15,18]])
    c = s.merge([[1,4],[0,2],[3,5]])
    print(c)