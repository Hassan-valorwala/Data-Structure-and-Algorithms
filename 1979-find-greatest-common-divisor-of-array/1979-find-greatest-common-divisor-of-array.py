class Solution:
    def findGCD(self, nums: list[int]) -> int:
        small = min(nums)
        big = max(nums)
        while small > 0 and big > 0:
            if small > big:
                small = small % big
            else:
                big = big%small
        if big == 0:
            return small
        else:
            return big                

        