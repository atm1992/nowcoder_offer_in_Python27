# -*- coding: UTF-8 -*-
"""
数字在排序数组中出现的次数。
统计一个数字在排序数组中出现的次数。

解题思路：若不使用data.index(k)，则可考虑二分查找
"""


class Solution1:
    def GetNumberOfK(self, data, k):
        if not data or k not in data:
            return 0
        count = 1
        for i in range(data.index(k) + 1, len(data)):
            if data[i] == k:
                count += 1
            else:
                break
        return count


class Solution2:
    def GetNumberOfK(self, data, k):
        return data.count(k)


class Solution3:
    # 二分查找
    def GetNumberOfK(self, data, k):
        if not data or self.GetLastK(data, k) < 0:
            return 0
        return self.GetLastK(data, k) - self.GetFirstK(data, k) + 1

    def GetLastK(self, data, k):
        low = 0
        high = len(data) - 1
        # 二分查找的这里必须是<=，例如：只有两个元素，待查找元素等于第二个元素
        while low <= high:
            mid = (low + high) // 2
            if data[mid] > k:
                high = mid - 1
            elif data[mid] < k:
                low = mid + 1
            else:
                if mid == high or data[mid + 1] != k:
                    return mid
                else:
                    low = mid + 1
        return -1

    def GetFirstK(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] > k:
                high = mid - 1
            elif data[mid] < k:
                low = mid + 1
            else:
                if mid == low or data[mid - 1] != k:
                    return mid
                else:
                    high = mid - 1
        return -1
