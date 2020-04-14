#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   findSubstring.py
@Time    :   2020/04/14 14:00:29
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """ TLS """
        from collections import Counter
        res = []
        if not (s and words):
            return res
        left = 0
        min_len = len(words[0])
        right = min_len
        marked = Counter(words)
        while right <= len(s):
            start = left
            while s[left:right] in words:
                word = s[left:right]
                if marked[word] <= 0:
                    break
                else:
                    marked[word] -= 1
                if sum(marked.values()) == 0:
                    res.append(start)
                    break
                left = right
                right = left + min_len
            marked = Counter(words)
            left = start + min_len
            right = left + min_len
        return res

    def findSubstring1(self, s: str, words: List[str]) -> List[int]:
        """ 1184 ms	13.9 MB """
        from collections import Counter
        if not (words and s):
            return []
        one_word = len(words[0])
        all_len = one_word * len(words)
        marked = Counter(words)
        n = len(s)
        res = []
        for i in range(0, n - all_len + 1):
            temp = s[i:i+all_len]
            c_temp = []
            for j in range(0, all_len, one_word):
                c_temp.append(temp[j:j+one_word])
            if Counter(c_temp) == marked:
                res.append(i)
        return res

    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not (words and s):
            return []
        one_word = len(words[0])
        n = len(s)
        word_num = len(words)
        marked = Counter(words)
        res = []
        # 为什么范围是这个，没理解！
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_counter = Counter()
            while right <= n - one_word:
                w = s[right:right+one_word]
                cur_counter[w] += 1
                cur_cnt += 1
                right += one_word
                while cur_counter[w] > marked[w]:
                    left_w = s[left:left+one_word]
                    left += one_word
                    cur_counter[left_w] -= 1
                    cur_cnt -= 1
                if cur_cnt == word_num:
                    res.append(left)
        return res


if __name__ == '__main__':
    s = Solution()
   # c = s.findSubstring3("wordgoodgoodgoodbestword", ["word","good","best","word"])
   # c = s.findSubstring3("barfoothefoobarman", ["foo","bar"])
    c = s.findSubstring2("barfoofoobarthefoobarman", ["bar","foo","the"])
    #c = s.findSubstring2("wordgoodgoodgoodbestword", ["word","good","best","good"])
    #c = s.findSubstring("a", ["a"])
    print(c)
