"""
Counting Rock Samples | TCS Codevita 2020
John is a geologist, and he needs to count rock samples in order to send it to a chemical laboratory. He has a problem. The laboratory only accepts rock samples by a range of sizes in ppm (parts per million). John needs your help. Your task is to develop a program to get the number of rocks in each range accepted by the laboratory.

Problem Statement: Given an array samples[] denoting sizes of rock samples and a 2D array ranges[], the task is to count the rock samples that are in the range ranges[i][0] to ranges[i][1], for every possible 1 <= i <= N.
"""
samples1 = [345, 604, 321, 433, 704, 470, 808, 718, 517, 811]
ranges1 = [[300, 380], [400, 700]]
class Solution:
    def findRockSample(self, samples, ranges):
        N = len(ranges)
        res =[]
        for i in range(N):
            count = 0
            s, e = ranges[i][0], ranges[i][1]
            for rock in samples:
                if s <= rock <= e:
                    count += 1
            res.append(count)
        return res
sol = Solution()
print(sol.findRockSample(samples1, ranges1)) #[2, 4]

