class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = []
        a = temperatures

        for x in range(len(a)):
            found = False
            for y in range(x + 1, len(a)):
                if a[y] > a[x]:
                    count = y - x
                    out.append(count)
                    found = True
                    break
            if not found:
                out.append(0)

        return out
            



        