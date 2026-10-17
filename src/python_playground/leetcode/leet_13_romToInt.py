class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M':1000}
        ans = 0
        for a,b in zip(s,s[1:]):
            if my_dict[a] < my_dict[b]:
                ans -= my_dict[a]
            else:
                ans += my_dict[a]
        return ans + my_dict[s[-1]]

    # best solution
    def romanToInt_best(self, s: str) -> int:
        track = "none"
        pairD = {"V":"I", "X":"I", "L":"X", "C":"X", "D":"C", "M":"C"}
        valueR = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        value = 0
        
        for i in range(len(s) - 1, -1, -1):
            if track == "none":
                if s[i] in pairD:
                    track = pairD[s[i]]
                value += valueR[s[i]]
            else:
                if s[i] == track:
                    value -= valueR[s[i]]
                    track = "none"
                else:
                    track = pairD[s[i]]
                    value += valueR[s[i]]
        return value
