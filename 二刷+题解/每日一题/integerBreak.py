# -*- encoding: utf-8 -*-
'''
@File    :   integerBreak.py
@Time    :   2020/09/10 14:36:33
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def integerBreak(self, n: int) -> int:
        memory = [1 for _ in range(n+1)]
        memory[2] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                memory[i] = max(memory[i], max(j * memory[i - j], j * (i - j)))
        return memory[n]

if __name__ == '__main__':
    pass