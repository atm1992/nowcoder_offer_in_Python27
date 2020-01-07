# -*- coding:utf-8 -*-
"""
表示数值的字符串。
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

解题思路：一步步排除不是数值的情况，若所有异常情况都不符合，则返回True
"""


class Solution:
    # s字符串
    def isNumeric(self, s):
        if len(s) < 1:
            return False
        # 分别标记是否出现过正负号、小数点、e。因为这几个需要特殊考虑
        has_sign = False
        has_point = False
        has_e = False
        sLen = len(s)
        for i in range(sLen):
            # 对于e的情况。确保至多出现一个e，并且不是出现在最末尾或开头的位置
            if s[i] == 'E' or s[i] == 'e':
                # 若前面已经出现过e，则直接返回False。因为不能出现两个e
                if has_e:
                    return False
                else:
                    has_e = True
                    # 若e出现在字符串的最末尾或开头，则直接返回False
                    if i == sLen - 1 or i == 0:
                        return False
            # 对于符号位的情况。确保符号位出现在第一个位置或者紧随在e的后面
            elif s[i] == '+' or s[i] == '-':
                # 若前面已经出现过符号位，则此时的符号位只能紧跟在e的后面
                if has_sign and s[i - 1] != 'E' and s[i - 1] != 'e':
                    return False
                # 若是第一次出现符号位
                else:
                    has_sign = True
                    # 若该符号位不是在字符串的第一个位置，并且前面也不是e，则直接返回False
                    if i > 0 and s[i - 1] != 'E' and s[i - 1] != 'e':
                        return False
            # 考虑小数点的情况。确保至多出现一个小数点并且不是在e的后面
            elif s[i] == '.':
                # 若前面已经出现了小数点或者e，则直接返回False。因为不能出现两个小数点，以及e的后面必须是整数
                if has_point or has_e:
                    return False
                # 第一次出现小数点，并且前面没有e
                else:
                    has_point = True
            # 考虑其它字符。确保其它字符都在0~9之间
            else:
                # 其它字符必须是在'0'到'9'之间。
                # 注意：这里比较大小不能使用int(s[i])，因为s[i]未必是数字，直接使用int()转换类型来比较大小可能会报错
                # 字符之间比较大小比的是ASCII码大小。ord('a') 可获得'a'的ASCII码值；chr(97)可获得ASCII码值为97的字符
                if s[i] < '0' or s[i] > '9':
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isNumeric("-1E-16"))
