class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for pos, speed in sorted(zip(position, speed), reverse = True):
            steps = (target - pos) / speed

            if not stack or steps > stack[-1]:
                stack.append(steps)

        return len(stack)