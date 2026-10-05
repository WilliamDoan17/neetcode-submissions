class Solution:
    def encode(self, strs: list[str]) -> str:
        return ''.join([str(len(s)) + '#' + s for s in strs])

    def decode(self, s: str) -> list[str]:
        n = len(s)
        cur_len = 0 
        next_stop = 0
        result = []
        i = 0
        while i < n:
            if s[i] == '#':
                next_stop = i + cur_len
                result.append(''.join(s[i + 1 : next_stop + 1]))
                i = next_stop
                cur_len = 0
            else:
                cur_len = cur_len * 10 + (ord(s[i]) - ord('0'))
            i += 1
        return result
