# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(n, nums, arr):
            for i in range(len(nums)):
                arr[i] = nums[i]

            left, right = 0, n
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]   
                left += 1
                right -= 1

            return arr

        k_values = []
        for i in range(len(arr) - 1, 0, -1):
            nums = arr[:i+1]
            max_element = max(nums)
            index = nums.index(max_element)
            k_values.append(index + 1)
            nums = nums[:index + 1]

            nums = nums[::-1]
            arr = flip(i, nums, arr)

        return k_values
