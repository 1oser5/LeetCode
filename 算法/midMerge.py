#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   midMerge.py
@Time    :   2019/12/08 14:56:29
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
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
        m = len(intervals)-1
        l = sorted(intervals, key=lambda x: x[0])
        for i in range(m):
            if l[i][1] >= l[i+1][0]:
                l[i+1] = [min(l[i][0], l[i+1][0]), max(l[i+1][1], l[i][1])]
                l[i] = ['#','#']
        return [i for i in l if i[0] != '#']   
if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))