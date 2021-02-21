#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/2/20 10:28 下午
# @file : 53-0～n-1中缺失的数字.py
# @software : PyCharm

'''
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3]
输出: 2

示例 2:
输入: [0,1,2,4,5,6,7,8,9]
      0 1 2 3 4 5 6 7 8
输出: 8

限制：

1 <= 数组长度 <= 10000
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)-1
        while i<=j:
            mid = (i + j) // 2
            if nums[mid]==mid:
                i=mid+1
            else:
                j=mid-1
        return i

print('w w'.replace(' ','%20'))

a=[0]
print(Solution().missingNumber(a))