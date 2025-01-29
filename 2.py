"""
Array Reverse
Given an array arr[], the task is to reverse the array. 
Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.
"""
arr1 = [1, 4, 3, 2, 6, 5]
arr2 = [4, 5, 1, 2]
class Solution:
    def reverse(self, arr):
        N = len(arr)
        for i in range(N//2):
            temp = arr[i]
            arr[i] = arr[N - 1 - i]
            arr[N - 1 - i] = temp
        return arr
sol = Solution()
print(sol.reverse(arr1)) #[5, 6, 2, 3, 4, 1]
print(sol.reverse(arr2)) #[2, 1, 5, 4]
