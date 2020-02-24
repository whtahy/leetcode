class Solution:
    def minWindow(self, s: str, t: str) -> str:
        set_t = set(t)
        target_counts = {ch: t.count(ch) for ch in set_t}
        window_counts = {ch: 0 for ch in set_t}

        window = collections.deque()
        left, right = 0, len(s)

        for i, ch in enumerate(s):
            if ch not in window_counts.keys():
                continue

            window.append(i)
            window_counts[ch] += 1

            if all(window_counts[ch] >= target_counts[ch] for ch in target_counts):
                l, r = window[0], window[-1]

                if r - l < right - left:
                    left, right = l, r
                if right - left + 1 == len(t):
                    break

                window_counts[s[window[0]]] -= 1
                window.popleft()

            while window_counts[s[window[0]]] > target_counts[s[window[0]]]:
                window_counts[s[window[0]]] -= 1
                window.popleft()

        if right < len(s):
            return s[left:right+1]
        else:
            return ""
