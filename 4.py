"""
Second Largest Element in an Array
Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.

Note: If the second largest element does not exist, return -1.
"""
arr1 = [2]
arr2 = [2, 3, 1, 4, 10, 9, 8]
arr3 = [10, 10, 10]
class Solution:
    def secondLargest(self, arr):
        arr.sort()
        N = len(arr)
        if N < 2:
            return -1
        if arr[N - 2] == arr[N - 1]:
            return -1 
        return arr[N - 2]
sol = Solution()
print(sol.secondLargest(arr1)) #-1
print(sol.secondLargest(arr2)) #9
print(sol.secondLargest(arr3)) #-1

    