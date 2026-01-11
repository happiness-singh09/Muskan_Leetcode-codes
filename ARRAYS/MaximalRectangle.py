class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        max_area = 0
        heights = [0] * len(matrix[0])
        for row in matrix:
            for i in range(len(matrix[0])):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area
    def largestRectangleArea(self, heights):
        stack = []
        max_hist_area = 0
        for i in range(len(heights) + 1):
            current_height = heights[i] if i < len(heights) else 0
            while stack and heights[stack[-1]] >= current_height:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_hist_area = max(max_hist_area, h * w)
            stack.append(i)
        return max_hist_area