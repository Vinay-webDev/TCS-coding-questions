"""
Find first non-repeating element in a given Array of integers

Given an array of integers of size N, 
the task is to find the first non-repeating element in this array. 
"""
arr1 = [-1, 2, -1, 3, 0]
arr2 = [9, 4, 9, 6, 7, 4]
class Solution:
    def nonRepeating(self, arr):
        N, arr_count = len(arr), {}
        for i in range(N):
            if arr[i] not in arr_count:
                arr_count[arr[i]] = 1
            else:
                arr_count[arr[i]] += 1
        res = 0
        for j in range(N):
            if arr_count[arr[j]] == 1:
                return arr[j]
sol = Solution()
print(sol.nonRepeating(arr1))   #2
print(sol.nonRepeating(arr2))   #6








