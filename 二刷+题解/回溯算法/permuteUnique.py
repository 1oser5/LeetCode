#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   permuteUnique.py
@Time    :   2020/04/07 14:34:55
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(temp, l):
            if not l:
                res.append(temp)
            for index, num in enumerate(l):
                # 减枝
                if index > 0 and num == l[index-1]:
                    continue
                helper(temp+[num], l[:index]+l[index+1:])
        helper([], sorted(nums)) # 排序是为了减枝
        print(res)
        return res
if __name__ == '__main__':
    s = Solution()
    s.permuteUnique([3,3,0,3])