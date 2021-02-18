# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/2/18 9:38 下午
# @file : 04-二维数组中的查找.py
# @software : PyCharm

'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

给定 target = 5，返回 true。
给定 target = 20，返回 false。

限制：

0 <= n <= 1000
0 <= m <= 1000
'''

a = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24]
]


# 二叉树法，旋转45度
class Solution:
    def findNumberIn2DArray(self, matrix: list, target: int) -> bool:
        if not matrix:
            return False
        i = len(matrix[0]) - 1
        j = 0
        while i >= 0 and j < len(matrix):
            root = matrix[j][i]
            if target == root:
                return True
            elif target < root:
                i -= 1
            elif target > root:
                j += 1
        return False


print(Solution().findNumberIn2DArray(a, 5))
