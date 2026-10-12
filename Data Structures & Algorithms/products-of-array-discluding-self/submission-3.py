class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = False
        multiple = False
        total = 0
        for num in nums:
            if (num != 0):
                if total == 0:
                    total = num
                else:
                    total = total * num
            elif zero:
                multiple = True
            else:
                zero = True
        ans = []
        if multiple:
            for num in nums:
                ans.append(0)
            return ans

        if zero:
            for num in nums:
                if num == 0:
                    ans.append(total)
                else:
                    ans.append(0)
        else:      
            for num in nums:
                ans.append(int(total/num)) 
        

        return ans