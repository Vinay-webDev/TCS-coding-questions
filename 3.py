"""
Largest element in an Array
Given an array arr. The task is to find the largest element in the given array. 
"""
arr1 = [1, 2, 3, 4, 5]
arr2 = [10, 100, 28, 83, 103, 99]
class Solution:
    def largest(self, arr):
        N, maxx = len(arr), 0
        for i in range(N):
            if arr[i] > maxx:
                maxx = arr[i]
        return maxx
sol = Solution()
print(sol.largest(arr1))  #5
print(sol.largest(arr2))  #103


