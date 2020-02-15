class Helper:
    def __init__(self, x):
        self.n = 0
        self.s = ""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = Helper(n)
        out = [s]

        for i in range(n*2):
            for p in out[:len(out)]:
                if p.n == 0:
                    # open
                    p.s += "("
                    p.n += 1
                    continue
                if p.n < n and n*2-i > p.n:
                    # open
                    open = Helper(n)
                    open.n = p.n + 1
                    open.s = p.s + "("
                    out += [open]
                # close
                p.s += ")"
                p.n -= 1

        return [p.s for p in out]
