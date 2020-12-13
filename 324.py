import random
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def quickselect(low, hight, k, arr):
            pivot = random.randint(low, hight)
            arr[pivot], arr[hight] = arr[hight], arr[pivot]
            pivot = low
            for i in range(low, hight):
                if arr[i] < arr[hight]:
                    arr[i], arr[pivot] = arr[pivot], arr[i]
                    pivot += 1
            arr[pivot], arr[hight]= arr[hight], arr[pivot]

            if k < pivot:
                quickselect(low, pivot - 1, k, arr)
            elif k > pivot:
                quickselect(pivot + 1, hight, k, arr)
            else:
                return arr[k]

        median = quickselect(0, len(nums) - 1, len(nums) // 2, nums)

        mid = len(nums) // 2

        vi = lambda x: 2 * x + 1 if x < mid else (x - mid) * 2

        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[vi(j)] < median:
                nums[vi[j]], nums[vi[k]] = nums[vi[k]], nums[vi[j]]
                k -= 1
            elif nums[vi(j)] > median:
                nums[vi(i)], nums[vi(j)] = nums[vi(j)], nums[vi(i)]
                i += 1
                j += 1
            else:
                j += 1

s = Solution()
s.wiggleSort([1,5,1,1,6,4])