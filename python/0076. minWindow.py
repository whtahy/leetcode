class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = collections.deque()
        window_counts = {k: -v for k, v in collections.Counter(t).items()}

        counter = 0
        left, right = 0, len(s)

        for i, ch in enumerate(s):
            if ch not in window_counts:
                continue

            if window_counts[ch] < 0:
                counter += 1

            window.append(i)
            window_counts[ch] += 1

            # window not full
            if counter < len(t):
                continue

            while window_counts[s[window[0]]] > 0:
                window_counts[s[window[0]]] -= 1
                window.popleft()

            l, r = window[0], window[-1]

            if r-l < right-left:
                left, right = l, r
            if right-left+1 == len(t):
                break

            # speed up
            window_counts[s[window[0]]] -= 1
            if window_counts[s[window[0]]] < 0:
                counter -= 1
            window.popleft()

        if right == len(s):
            return ""

        return s[left:right+1]
