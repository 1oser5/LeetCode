#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   letterCombinations.py
@Time    :   2019/11/30 10:18:09
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        """40 ms	13.9 MB"""
        if not s: return []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        def foo(s, c):
            if len(c) == len(digits): return res.append(c)
            for i in d[digits[s]]:
                foo(s+1, c+i)
        foo(0,'')
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))