#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   minimumLengthEncoding.py
@Time    :   2020/05/21 10:28:50
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List


class Trie(object):
    def __init__(self):
        self.look_up = {}

    def insert(self, word):
        isNew = False
        tree = self.look_up
        for w in word:
            if w not in tree:
                tree[w] = {}
                isNew = True
            tree = tree[w]
        return len(word)+1 if isNew else 0

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        ''' 前缀树解法 '''
        words = sorted(words, key=lambda x: len(x), reverse=True)
        trie = Trie()
        res = 0
        for word in words:
            res += trie.insert(word[::-1])
        return res

    def minimumLengthEncoding(self, words: List[str]) -> int:
        ''' 排序检查解法 '''
        reversed_word = []
        size = len(words)
        for word in words:
            reversed_word.append(word[::-1])
        res = 0
        reversed_word.sort()
        for i in range(len(reversed_word)):
            if i + 1 < size and reversed_word[i+1].startswith(reversed_word[i]):
                continue
            res += len(reversed_word[i]) + 1
        return res





if __name__ == '__main__':
    s = Solution()
    c = s.minimumLengthEncoding(["time", "me", "bell"])
    print(c)