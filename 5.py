"""
Counting frequencies of array elements
Given an array which may contain duplicates, print all elements and their frequencies.
"""
arr1 = [10, 20, 20, 10, 10, 20, 5, 20]
arr2 = [10, 20, 20]
class Solution:
    def frequency(self, arr):
        count = {}
        N = len(arr)
        for i in range(N):
            if arr[i] not in count:
                count[arr[i]] = 1
            else:
                count[arr[i]] += 1
        return count
sol = Solution()
print(sol.frequency(arr1))  #{10: 3, 20: 4, 5: 1}
print(sol.frequency(arr2))  #{10: 1, 20: 2}









