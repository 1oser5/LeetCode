#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   permutation.py
@Time    :   2020/04/24 09:04:01
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        """ 巨慢无比 """
        res = []

        def helper(t, p):
            if not p and t not in res:
                res.append(t)
            visited = set()
            for i, v in enumerate(p):
                if (len(t), v) in visited:
                    continue
                visited.add((len(t), v))
                helper(t+v, p[:i] + p[i+1:])
        helper('', s)
        return res

    def permutation1(self, s: str) -> List[str]:
        c, res = list(s), []

        def dfs(x):
            if x == len(s) - 1:
                res.append(''.join(c))
                return
            memory = set()
            for i in range(x, len(c)):
                if c[i] in memory:
                    continue
                memory.add(c[i])
                c[x], c[i] = c[i], c[x]
                dfs(x+1)
                c[x], c[i] = c[i], c[x]
        dfs(0)
        return res
if __name__ == '__main__':
    s = Solution()
    c = s.permutation("aab")
    print(c)