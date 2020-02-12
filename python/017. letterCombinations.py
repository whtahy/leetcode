class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        combinations = []
        for letter in digits:
            if letter in phone_map:
                combinations = Solution.cartesian(combinations, phone_map[letter])

        return combinations

    def cartesian(a, b):
        if a:
            return [x + y for x in a for y in b]
        else:
            return list(b)
