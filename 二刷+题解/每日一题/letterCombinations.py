# -*- encoding: utf-8 -*-
'''
@File    :   letterCombinations.py
@Time    :   2020/08/26 09:12:50
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        res = []
        def backtrack(s, p):
            if len(p) == len(digits):
                res.append(p)
                return
            for c in dictionary[s[0]]:
                backtrack(s[1:], p + c)
        backtrack(digits, '')
        return res
if __name__ == '__main__':
    s = Solution()
    s.letterCombinations('23')