"""
Program to find sum of elements in a given array
Given an array of integers, find the sum of its elements.
"""
arr1 = [1, 2, 3, 4, 5]
arr2 = [0, 100, 393, 10]
class Solution:
    def cal_sum(self, arr):
        N, summ =len(arr), 0
        for i in range(N):
            summ += arr[i]
        return summ
sol = Solution()
print(sol.cal_sum(arr1))  #15
print(sol.cal_sum(arr2))  #503
        
        



