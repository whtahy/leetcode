class Solution:
    sign = r'[\+-]?'
    digit_dot = r'\d+\.?\d*'
    dot_digit = r'\d*\.?\d+'
    exponent = fr'(e{sign}\d+)'

    regex = re.compile(rf'^{sign}({digit_dot}|{dot_digit}){exponent}?$')

    def isNumber(self, s: str) -> bool:
        return Solution.regex.search(s.strip())
