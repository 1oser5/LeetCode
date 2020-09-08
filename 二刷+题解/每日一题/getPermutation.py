# -*- encoding: utf-8 -*-
'''
@File    :   getPermutation.py
@Time    :   2020/09/08 08:24:12
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(k, index, path):
            # 已经为叶子节点了,直接返回
            if index == n:
                return
            cnt = factorial[n - 1 - index]
            for i in range(1, n + 1):
                # 已使用过
                if used[i]:
                    continue
                # 不在该回溯分支中，减去分枝数，继续向后走
                if cnt < k:
                    k -= cnt
                    continue
                used[i] = True
                path.append(i)
                dfs(k, index+1, path)
                return   # 不需要继续向后遍历了
        if n == 0:
            return ''
        used = [False for _ in range(n+1)]
        factorial = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            factorial[i] = factorial[i-1] * i
        path = []
        dfs(k, 0, path)
        return ''.join([str(num) for num in path])



if __name__ == '__main__':
    pass