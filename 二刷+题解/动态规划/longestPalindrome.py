#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   longestPalindrome.py
@Time    :   2020/04/09 14:50:07
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def longestPalindrome(self, s: str) -> str:
        "manacher"



if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('cbbd'))
