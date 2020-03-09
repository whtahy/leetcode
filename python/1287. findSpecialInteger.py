# look ahead
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(n):
            if arr[i] == arr[i + n//4]:
                return arr[i]

# naive
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = 0
        ans = None
        for x in arr:
            if x == ans:
                n += 1
            else:
                n = 1
                ans = x
            if n > len(arr)//4:
                return ans
