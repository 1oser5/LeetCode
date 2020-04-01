#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   combinationSum2.py
@Time    :   2020/04/01 19:59:20
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 排序减枝
        candidates = sorted(candidates)

        def helper(temp, num, l):
            if num == 0:
                res.append(temp)
            for index, item in enumerate(l):
                # 减枝
                if num - item < 0:
                    return
                # 速度就差再去重上了
                if index != 0 and l[index-1] == l[index]:
                    continue
                helper(temp + [item], num - item, l[index + 1:])
        helper([], target, candidates)
        print(res)
        return res

# here put the import lib

if __name__ == '__main__':
    s = Solution()
    s.combinationSum2([10,1,2,7,6,1,5], 8)