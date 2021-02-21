# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/2/20 9:38 下午
# @file : 53-在排序数组中查找数字.py
# @software : PyCharm

'''
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

限制：
0 <= 数组长度 <= 50000
'''


# 计数法
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dict_nums = dict.fromkeys(nums, 0)
        for i in nums:
            dict_nums[i] += 1
        return dict_nums.get(target, 0)


class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def test(tar):
            i, j = 0, len(nums) - 1

            while i <= j:
                mid = (i + j) // 2
                if nums[mid] <= tar:
                    i = mid + 1
                else:
                    j = mid - 1
            return i
        return test(target)-test(target-1)








nums = [5, 7, 7, 8, 8, 10]
target = 8
print(Solution2().search(nums, target))
