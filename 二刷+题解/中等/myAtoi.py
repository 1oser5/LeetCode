#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   myAtoi.py
@Time    :   2020/05/29 09:19:21
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton(object):
    def __init__(self):
        # init start
        self.status = 'start'
        self.sign = 1
        self.ans = 0
        # init DFA rules
        self.table = {
            'start': ['start', 'sign', 'number', 'end'],
            'sign': ['end', 'end', 'number', 'end'],
            'number': ['end', 'end', 'number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c in '+-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.status = self.table[self.status][self.get_col(c)]
        if self.status == 'number':
            self.ans = self.ans * 10 + int(c)
            # handle edge
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.status == 'sign':
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, str: str) -> int:
        ''' 状态机 '''
        an = Automaton()
        for c in str:
            an.get(c)
        return an.sign * an.ans

if __name__ == '__main__':
    pass