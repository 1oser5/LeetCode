#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   permute.py
@Time    :   2019/11/25 20:36:17
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个没有重复数字的序列，返回其所有可能的全排列。

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
class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        '''80 ms	14 MB'''
        result = []
        def foo(l=[]):
            if len(l) == len(nums):
                return result.append(l.copy())
            for i in nums:
                if i not in l:
                    l.append(i)
                    foo(l)
                    l.pop()
        foo()
        return result
    
    def permute2(self, nums: [int]) -> [[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                return res.append(tmp)
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:],tmp + [nums[i]])
        backtrack(nums,[])
        return res
                    
if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
    print(s.permute2([1,2,3]))