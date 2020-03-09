class NumArray:
    def __init__(self, nums: List[int]):
        self.ls = nums
        for i in range(1, len(nums)):
            self.ls[i] += self.ls[i-1]
        print(self.ls)

    def sumRange(self, i: int, j: int) -> int:
        return self.ls[j] - (self.ls[i-1] if i > 0 else 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
