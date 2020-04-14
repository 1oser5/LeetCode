#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   lengthOfLongestSubstring.py
@Time    :   2020/04/14 13:37:53
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = set()
        left = 0
        right = 0
        m_len = 0
        while right <= len(s) - 1:
            while right <= len(s) - 1 and s[right] not in m:
                m.add(s[right])
                right += 1
            m_len = max(m_len, right-left)
            m.remove(s[left])
            left += 1
        return m_len

    def lengthOfLongestSubstring1(self, s: str) -> int:
        lookup = set()
        left = 0
        m_len = 0
        c_len = 0
        for i in range(len(s)):
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                c_len -= 1
            lookup.add(s[i])
            c_len += 1
            m_len = max(m_len, c_len)
        return m_len


if __name__ == '__main__':
    s = Solution()
    #c = s.lengthOfLongestSubstring('abcabcbb')
    c = s.lengthOfLongestSubstring1('au')
    print(c)