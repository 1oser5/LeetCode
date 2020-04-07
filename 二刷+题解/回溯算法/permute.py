#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   permute.py
@Time    :   2020/04/07 14:09:49
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(temp, l):
            if not l:
                res.append(temp)
                return
            for index, num in enumerate(l):
                helper(temp + [num], l[:index] + l[index+1:])
        helper([], nums)
        print(res)
        return res

if __name__ == '__main__':
    s = Solution()
    s.permute([1,2,3])