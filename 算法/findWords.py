#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   findWords.py
@Time    :   2020/01/05 14:05:54
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
from pprint import pprint
from collections import defaultdict
class TrieNode(object):
        def __init__(self):
            self.children = defaultdict(TrieNode)
            self.isWord = False
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        m = len(board)
        n = len(board[0])
        for word in words:
            trie.insert(word)
        for i in range(m):
            for j in range(n):
                self.dfs(board, trie.root, i, j, "", res)
        return res
    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j<0 or j >= len(board[0]): return
        temp = board[i][j]
        node = node.children.get(temp)
        if not node: return
        board[i][j] = '#'
        self.dfs(board, node, i-1, j, path+temp, res)
        self.dfs(board, node, i+1, j, path+temp, res)
        self.dfs(board, node, i, j-1, path+temp, res)
        self.dfs(board, node, i, j+1, path+temp, res)
        board[i][j] = temp

if __name__ == '__main__':
    s = Solution()
    # p = s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])
    # p = s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath"])
    p = s.findWords([["a","b"],["c","d"]],["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"])
    # p = s.findWords([['a','b']],['ab'])
    print(p)