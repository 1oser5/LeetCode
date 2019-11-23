#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   subsets.py
@Time    :   2019/11/23 19:35:59
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

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
class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        '''48 ms	14.1 MB'''
        result = [[]]
        def foo(m):
            if len(m) > 1:
                for s in foo(m[1:]):
                    result.append(s+[m[0]])
            else:
                result.append(m)
            return result.copy()
        foo(nums)
        return result
    def subsets2(self, nums: [int]) -> [[int]]:
        '''这个迭代秒杀我写的'''
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res
    def subsets3(self, nums: [int]) -> [[int]]:
        res = []
        n = len(nums)
        def helper(j,tem):
            res.append(tem)
            for i in range(j,n):
                helper(i+1,tem+[nums[i]])
        helper(0,[])
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))
    print(s.subsets2([1,2,3]))
    print(s.subsets3([1,2,3]))