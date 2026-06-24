class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for current in range(len(temperatures)):
            while stack and temperatures[current] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = current - prev_day
            stack.append(current)
        return res