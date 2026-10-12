class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sorted_numbers = numbers[:]
        sorted_numbers.sort()
        l, r = 0, len(numbers) - 1

        while l < r:
            s = sorted_numbers[l] + sorted_numbers[r]
            if s == target:
                left, right = None, None
                for i, n in enumerate(numbers):
                    if not left and n == sorted_numbers[l]:
                        left = i + 1
                    elif n == sorted_numbers[r]:
                        right = i + 1
                return [left, right]
            elif s > target:
                r -= 1
            else:
                l += 1

        return -1

