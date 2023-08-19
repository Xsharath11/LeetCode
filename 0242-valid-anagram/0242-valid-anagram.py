class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        l = {}
        for i in s:
            if i not in l:
                l[i] = 1

            else:
                l[i] += 1

        for i in t:
            if i not in d:
                d[i] = 1

            else:
                d[i] += 1
                

        return l == d


            