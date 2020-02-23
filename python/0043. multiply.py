class Solution:
    def helper(s):
        return [int(x) * 10 ** (len(s)-i-1) for i, x in enumerate(s)]

    def multiply(self, num1: str, num2: str) -> str:
        a = Solution.helper(num1)
        b = Solution.helper(num2)
        product = 0
        for x in a:
            for y in b:
                product += x * y
        return f"{product}"
