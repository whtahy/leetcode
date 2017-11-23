class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        ls = sorted(nums1 + nums2)
        l = len(ls)
        i = (l-1)//2
        if l % 2 == 1:
            return ls[i]
        else:
            return (ls[i] + ls[i+1]) / 2
