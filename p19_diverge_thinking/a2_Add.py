# -*- coding: UTF-8 -*-
"""
不用加减乘除做加法。
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

解题思路：位运算。
a^b 得到没有进位的和
(a&b)<<1 得到进位
"""


class Solution:
    def Add(self, num1, num2):
        # 当进位为0时，退出循环
        while num2 != 0:
            # num1表示没有进位的和；num2表示进位，进位每次都左移一位，然后右侧补0，最终进位会等于0
            # 之所以要在后面加上&0xffffffff，是因为int整数的长度为32位，若不限定，随着进位不断左移，Python会将int隐式转换为long，而不会溢出。
            # 从而导致进位一直不等于0，进入无限循环，运行超时
            num1, num2 = (num1 ^ num2) & 0xffffffff, ((num1 & num2) << 1) & 0xffffffff
        # 根据最高位符号位（第32位）来判断num1是正数还是负数
        # 计算机内部使用二进制补码形式来存储数据，无论是正负数。Python位运算也是作用在补码上的，因此这里的num1是一个二进制补码
        return num1 if num1 <= 0x7fffffff else ~(num1 ^ 0xffffffff)


if __name__ == '__main__':
    s = Solution()
    print s.Add(-2, 1)
