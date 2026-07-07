class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        a = set(nums)
        longest = 0

        for b in a:
            # Start only if b is the beginning of a sequence
            if b - 1 not in a:
                count = 1
                while b + 1 in a:
                    b += 1
                    count += 1

                longest = max(longest, count)

        return longest