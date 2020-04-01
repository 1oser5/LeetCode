#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   combinationSum.py
@Time    :   2020/04/01 14:51:11
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

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
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """ 我的解法 """

        res = []

        def helper(num, temp):
            if num == 0 and sorted(temp) not in res:
                res.append(sorted(temp))
            if num < 0:
                return
            for candidate in candidates:
                helper(num - candidate, temp + [candidate])
        helper(target, [])
        print(res)
        return res

    def residueCombinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """ 结合 减枝 策略，减少递归次数

        1.将 candidates 进行排序，配合减枝
        2.如果当前 num < 0 则不需要进行，由于有序递增特点，不需要继续递归了

        """
        res = []
        candidates = sorted(candidates)
        def helper(temp, num, start, end):
            if num == 0:
                res.append(temp)
                return
            for index in range(start, end):
                # 减枝
                if num - candidates[index] < 0:
                    return
                helper(temp + [candidates[index]], num - candidates[index], index, end)
        helper([], target, 0, len(candidates))
        print(res)
        return res
if __name__ == '__main__':
    s = Solution()
    # s.residueCombinationSum([2,3,5], 8)
    # s.residueCombinationSum([2,3,6,7], 7)
    s.residueCombinationSum([8,7,4,3], 11)