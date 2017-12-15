class Solution:
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    def romanToInt(self, s):
        n,i = 0,0
        while i < len(s):
            if i + 1 < len(s) and s[i: i + 2] in Solution.d:
                n += Solution.d[s[i: i + 2]]
                i += 2
            else:
                n += Solution.d.get(s[i], 0)
                i += 1
        return n
