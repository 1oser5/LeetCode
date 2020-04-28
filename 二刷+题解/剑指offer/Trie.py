#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   Trie.py
@Time    :   2020/04/28 11:18:45
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.look_up = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.look_up
        for w in word:
            if w not in tree:
                tree[w] = {}
            tree = tree[w]
        tree['#'] = '#'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.look_up
        for w in word:
            if w not in tree:
                return False
            tree = tree[w]
        if '#' in tree:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.look_up
        for w in prefix:
            if w in tree:
                tree = tree[w]
            else:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':
    pass