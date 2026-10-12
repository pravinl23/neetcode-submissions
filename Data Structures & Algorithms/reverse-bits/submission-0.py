class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(bin(n))
        n = n[2:]
        n = (32 - len(n)) * "0" + n
        n = n[::-1]
        
        binary = 0
        for bit in n:
            if bit == "1":
                binary = (binary << 1) | 1
            if bit == "0":
                binary = (binary << 1)

        return binary