#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   subsets.py
@Time    :   2020/04/01 09:34:47
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
""" 这是我的笨笨的办法 """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def generate(l, index):
            if len(l) > len(nums):
                return
            if sorted(l) not in res:
                res.append(sorted(l))
            for num in nums[index:]:
                if num not in l:
                    l.append(num)
                    generate(l, index+1)
                l.pop()
        generate([], 0)
        print(res)
        return(res)

    def cycle_subsets(self, nums: List[int]) -> List[List[int]]:
        """
        作者：powcai
        链接：https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

        这个迭代算法思路非常的清奇，通过 新值 对 res 列表的各项值相加，来获得子集

        """
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

    def helper_subsets(self, nums: List[int]) -> List[List[int]]:
        """

        作者：powcai
        链接：https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

        回溯算法
        """
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res





if __name__ == '__main__':
    s = Solution()
    s.subsets([1,2,3])