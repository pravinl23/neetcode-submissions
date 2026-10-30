class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
                continue

            while stack and a < 0 and stack[-1] > 0 and abs(stack[-1]) < abs(a):
                stack.pop()

            
            if not stack:
                stack.append(a)
            elif (stack[-1] + a) == 0:
                stack.pop()
                continue
            elif stack[-1] > abs(a):
                continue
            else:
                stack.append(a)
            

        return stack

