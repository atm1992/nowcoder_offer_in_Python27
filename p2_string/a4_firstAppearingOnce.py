# -*- coding:utf-8 -*-
"""
字符流中第一个不重复的字符。
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。

解题思路：使用一个字典来保存字符的出现次数，因为字典中的元素不是按出现次序保存，所以还需使用一个数组来按字符的出现次序保存所有字符
"""


class Solution:
    # 返回对应char
    def __init__(self):
        self.dic = {}
        self.lis = []

    def FirstAppearingOnce(self):
        for i in self.lis:
            if self.dic[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        if char not in self.dic.keys():
            self.dic[char] = 1
            self.lis.append(char)
        else:
            self.dic[char] += 1
