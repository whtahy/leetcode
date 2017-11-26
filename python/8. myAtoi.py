class Solution:
    def trunc(self, x):
        x_min, x_max = -(2 ** 31), 2 ** 31 - 1
        if x > x_max:
            return x_max
        elif x < x_min:
            return x_min
        else:
            return x

    def myAtoi(self, s):
        re_int = re.compile(r'^\s*([\+-]?\d+)')
        m = re_int.search(s)
        if m:
            return self.trunc(int(m.group()))
        else:
            return 0
