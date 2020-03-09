class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ls = []
        for freq, val in zip(nums[0::2], nums[1::2]):
            ls += [val] * freq
        return ls
