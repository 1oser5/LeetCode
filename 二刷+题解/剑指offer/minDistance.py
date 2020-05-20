#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   minDistance.py
@Time    :   2020/05/20 19:30:41
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ''' 自顶向下 因为字符串切片复杂度为 O(n)，效率不高'''
        if not word1 or word2:
            return len(word1) + len(word2)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            insert = self.minDistance(word1, word2[1:]) + 1
            delete = self.minDistance(word1[1:], word2) + 1
            replace = self.minDistance(word1[1:], word2[1:]) + 1
            return min(insert, delete, replace)

    def minDistance1(self, word1: str, word2: str) -> int:
        '''自顶向下 辅助函数 '''

        def helper(w1, w2):
            if w1 == len(word1) or w2 == len(word2):
                return len(word1) + len(word2) - (w1 + w2)
            if word1[w1] == word2[w2]:
                return helper(w1+1, w2+1)
            else:
                insert = helper(w1, w2+1)
                delete = helper(w1+1, w2)
                replace = helper(w1+1, w2+1)
                return min(insert, delete, replace) + 1
        return helper(0, 0)

    def minDistance2(self, word1: str, word2: str) -> int:
        ''' 自定向上 动态规划'''
        size1 = len(word1)
        size2 = len(word2)
        dp = [[0] * (size2+1) for _ in range(size1+1)]
        # 初始化，word1,word2任意一个为空字符串时，操作数另一字符长度
        for i in range(size1+1):
            dp[i][0] = i
        for j in range(size2+1):
            dp[0][j] = j
        for i in range(1, size1+1):
            for j in range(1, size2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]
if __name__ == '__main__':
    pass