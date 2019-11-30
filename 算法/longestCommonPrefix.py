#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   longestCommonPrefix.py
@Time    :   2019/11/29 19:52:07
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        """36 ms	14 MB"""
        if len(strs) == 0: return ''
        s  = sorted(strs, key= lambda i : len(i))
        m = len(s[0])
        c = 0
        while c < m:
            for i in strs:
                if s[0][c] != i[c]: return s[0][:c]   
            c += 1 
        return s[0]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))