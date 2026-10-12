class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while (True):
            if i == 0 and digits[i] + 1 == 10:
                digits.append(0)
                digits[0] = 1
                break
            if digits[i] + 1 < 10:
                digits[i] += 1
                break
            digits[i] = 0
            i -= 1
            
        return digits