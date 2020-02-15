class Solution:
    base = [1,4,5,9,10,40,50,90,100,400,500,900,1000][::-1]
    roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M'][::-1]

    def intToRoman(self, n):
        s = ''
        for i, x in enumerate(Solution.base):
            a = n // x
            n -= a * x
            s += a * Solution.roman[i]
        return s
