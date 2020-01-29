#-*- coding: UTF-8 -*-
"""
旋转数组的最小数字。
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如：数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

解题思路：若直接遍历整个数组，则时间复杂度为O(n)，并未使用到数组有序后旋转的特性。
因为数组刚开始是有序的，然后经过了一次旋转，因此这里可以使用二分查找的变体，将时间复杂度降为O(logn)
可将旋转数组看作两个非递减的子数组，前一个子数组中的所有元素均大于等于后一个子数组中的元素，这两个子数组的分界点就是所需查找的最小元素
使用两个指针：头指针刚开始指向第一个元素；尾指针指向最后一个元素。
头指针始终在前一个子数组内，结束时指向前一个数组的最大元素；尾指针始终在后一个子数组中，结束时指向后一个数组的最小元素。
退出循环的条件是尾指针索引比头指针大于1
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray or len(rotateArray) < 1:
            return 0
        low = 0
        high = len(rotateArray) - 1
        # 说明原有序数组没有旋转。若旋转了，数组的最后一个元素应该小于等于第一个元素
        if rotateArray[low] < rotateArray[high]:
            return rotateArray[low]
        # 原有序数组经过了旋转
        else:
            # 退出循环时，high等于low+1
            while high > low + 1:
                mid = (low+high) // 2
                # 特殊情况：low、mid、high所指向的值相等，此时退回顺序查找。例如：[1,1,1,0,1]
                if rotateArray[low] == rotateArray[mid] == rotateArray[high]:
                    min_val = rotateArray[low + 1]
                    for i in range(low + 2, high):
                        if rotateArray[i] < min_val:
                            min_val = rotateArray[i]
                    return min_val
                # 二分查找，右半部分
                elif rotateArray[mid] >= rotateArray[low]:
                    low = mid
                # 二分查找，左半部分
                else:
                    high = mid
            return rotateArray[high]


if __name__ == '__main__':
    s = Solution()
    arr = [
        6501, 6828, 6963, 7036, 7422, 7674, 8146, 8468, 8704, 8717, 9170, 9359, 9719, 9895, 9896, 9913, 9962, 154, 293, 334, 492, 1323, 1479, 1539,
        1727, 1870, 1943, 2383, 2392, 2996, 3282, 3812, 3903, 4465, 4605, 4665, 4772, 4828, 5142, 5437, 5448, 5668, 5706, 5725, 6300, 6335
    ]
    print(s.minNumberInRotateArray(arr))
