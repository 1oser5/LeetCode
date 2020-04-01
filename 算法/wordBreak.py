#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   wordBreak.py
@Time    :   2019/12/16 09:17:49
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_s = len(s)
        d = set(wordDict)
        dp = [False] * (len_s+1)
        dp[0] = True
        for i in range(len_s):
            for j in range(i+1,len_s+1):
                if dp[i] and (s[i:j] in d):
                    dp [j] = True
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("leetcode",["leet", "code"]))