class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                left_b = stack[-1] if stack else -1
                width = i - left_b - 1
                max_area = max(max_area , height * width)
            stack.append(i) 

        while stack:
                height = heights[stack.pop()]
                left_b = stack[-1] if stack else -1 
                width = len(heights) - left_b - 1
                max_area = max(max_area , height * width)
        return max_area
        