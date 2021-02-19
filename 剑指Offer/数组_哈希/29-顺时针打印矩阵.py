# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/2/19 8:21 下午
# @file : 29-顺时针打印矩阵.py
# @software : PyCharm

'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


限制：

    0 <= matrix.length <= 100
    0 <= matrix[i].length <= 100
'''


# 旋转法
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return None
        a = []
        while True:
            a += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
            if not matrix:
                break
        return a


# 边界法
class Solution2(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        left, right, top, below, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > below: break
            for i in range(top, below + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left: break
            for i in range(right, left-1, -1):
                res.append(matrix[below][i])
            below -= 1
            if below < top: break
            for i in range(below, top-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right: break
        return res


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(Solution2().spiralOrder(matrix))
