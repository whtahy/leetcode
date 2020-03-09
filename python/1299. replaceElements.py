class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = -1
        n = len(arr)
        for i, x in enumerate(reversed(arr)):
            arr[n-1-i] = m
            m = max(m, x)
        return arr
