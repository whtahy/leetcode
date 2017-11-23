class Solution:
    def myAtoi(self, s):
        n_min, n_max = -(2 ** 31), 2 ** 31 - 1

        def trunc(x, x_max=n_max, x_min=n_min):
            if x > x_max:
                return x_max
            elif x < x_min:
                return x_min
            else:
                return x

        re_int = re.compile(r'^\s*([\+-]?\d+)')
        m = re_int.search(s)
        if m:
            return trunc(int(m.group()))
        else:
            return 0
