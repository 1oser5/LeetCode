#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   subsetsWithDup.py
@Time    :   2020/04/07 14:58:14
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(temp, l):
            res.append(temp)
            for index, num in enumerate(l):
                # 减枝
                if index > 0 and l[index] == l[index-1]:
                    continue
                helper(temp+[num], l[index+1:])
        helper([], sorted(nums))
        return res
if __name__ == '__main__':
    s = Solution()
    c = s.subsetsWithDup([1,2,2])
    print(c)

