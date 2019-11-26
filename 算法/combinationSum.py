#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   combinationSum.py
@Time    :   2019/11/26 20:50:48
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        '''320 ms	13.8 MB'''
        res = []
        candidates.sort()
        def foo(num, l = [],c = 0):
            for i in range(c, len(candidates)):
                if num - candidates[i] < 0: return
                elif num - candidates[i] == 0: res.append(l + [candidates[i]])
                else: foo(num - candidates[i], l + [candidates[i]], i)
        foo(target)
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))