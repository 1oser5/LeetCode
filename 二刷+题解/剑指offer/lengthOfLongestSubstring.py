#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   lengthOfLongestSubstring.py
@Time    :   2020/04/26 18:48:52
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 

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
链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        left = 0
        memory = set()
        cur = 0
        for i in range(len(s)):
            cur += 1
            while left < i and s[i] in memory:
                memory.remove(s[left])
                left += 1
                cur -= 1
            memory.add(s[i])
            m = max(cur, m)
        return m

if __name__ == '__main__':
    s = Solution()
    c = s.lengthOfLongestSubstring("pwwkew")
    print(c)