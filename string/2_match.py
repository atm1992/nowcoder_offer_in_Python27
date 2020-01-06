# -*- coding:utf-8 -*-
"""
正则表达式匹配。
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。

解题思路：分情况讨论。递归思想
"""


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # 若s, pattern都为空，则返回True
        if len(s) == 0 and len(pattern) == 0:
            return True
        # 若s不为空,而pattern为空，则返回False
        elif len(s) != 0 and len(pattern) == 0:
            return False
        # 若s为空，而pattern不为空，则需分两种情况讨论
        elif len(s) == 0 and len(pattern) != 0:
            # 若pattern的第二个字符为*，则pattern后移两位继续比较
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])
            else:
                return False
        # 若s, pattern都不为空
        else:
            # 若pattern的第二个字符为*
            if len(pattern) > 1 and pattern[1] == '*':
                # 若s与pattern的第一个字符不相同，则s不变，pattern后移两位，相当于将pattern的前两位看为空。'*'代表0次
                if s[0] != pattern[0] and pattern[0] != '.':
                    return self.match(s, pattern[2:])
                # 若s[0]与pattern[0]相同，因为此时pattern[1]为'*'。则可分为三种情况：
                else:
                    # '*'代表0次 —— pattern后移两位，s不变，相当于将pattern的前两位看为空，匹配后面的
                    # '*'代表1次 —— pattern后移两位，s后移一位，相当于pattern前两位与s的第一位匹配
                    # '*'代表多次 —— pattern不变，s后移一位，相当于pattern前两位，与s中的多位进行匹配，因为*可以匹配多位
                    return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            # 若pattern的第二个字符不为*
            else:
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1:], pattern[1:])
                else:
                    return False
