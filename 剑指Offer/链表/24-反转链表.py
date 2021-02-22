# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/2/22 9:26 下午
# @file : 24-反转链表.py
# @software : PyCharm

'''
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。


示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

限制：
0 <= 节点个数 <= 5000
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        if not head:
            return None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
