class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n + 1):
            i = str(bin(i))
            output.append(i.count("1"))

        return output