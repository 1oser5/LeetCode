#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   lengthOfLongestSubstring.py
@Time    :   2019/11/27 13:39:48
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
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
        r = ''
        for _ in range(len(s)):
            a = ''
            for j in range(_, len(s)):
                if s[j] not in a: a += s[j]
                else: break
            r = a if len(a) > len(r) else r
        return len(r)
    
    def lengthOfLongestSubstring2(self, s: str) -> int:
        '''
        sliding window
        O(n)
        '''
        #最大长度
        m = 0
        #当前长度
        c = 0
        d = set()
        #滑动起点
        l = 0
        n = len(s)
        for i in range(n):
            c += 1
            while s[i] in d:
                d.remove(s[l])
                c -= 1
                l += 1
            m = max(m,c)
            d.add(s[i])
        return m

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(' '))
    print(s.lengthOfLongestSubstring2('pwwkew'))