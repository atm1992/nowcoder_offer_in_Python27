# -*- coding: UTF-8 -*-
"""
扑克牌顺子。
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,
看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,
他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。
LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。
为了方便起见,你可以认为大小王是0。

解题思路：先将数组排序，然后统计数组中大小王（也就是0）的个数，然后统计有序数组中相邻数字间的gap总数。若gap总数小于等于0的个数，则数组是连续的，否则不连续
注意：若数组中存在重复的非0数字，则表示存在对子，可直接判定数组不连续
"""


class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        n = len(numbers)
        # transdict = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        # for i in range(n):
        #     if numbers[i] in transdict.keys():
        #         numbers[i] = transdict[numbers[i]]
        numbers = sorted(numbers)
        # 统计数组中大小王（也就是0）的个数
        count_0 = numbers.count(0)
        # 统计需要使用大小王填补的空缺总数
        gaps = 0
        # 使用一前一后两个指针，前一个指针刚开始指向第一个非0数字，因为数组已经有序
        small = count_0
        big = small + 1
        while big < n:
            # 有序数组中的相邻两个数字相等，表示存在对子
            if numbers[small] == numbers[big]:
                return False
            # 之所以要减去1，是因为连续的两个数字之差原本就为1，而连续的两个数字之间无需使用大小王填补
            gaps += numbers[big] - numbers[small] - 1
            small = big
            big += 1
        return gaps <= count_0
