#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   checkInclusion.py
@Time    :   2020/04/14 17:09:10
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
 

示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import libs
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        s1_counter = Counter(s1)
        left = 0
        len_s1 = len(s1)
        right = len_s1
        n = len(s2)
        while right <= n:
            if Counter(s2[left:right]) == s1_counter:
                return True
            right += 1
            left += 1
        return False

if __name__ == '__main__':
    s = Solution()
    c = s.checkInclusion("ab","eidbaooo")
    print(c)