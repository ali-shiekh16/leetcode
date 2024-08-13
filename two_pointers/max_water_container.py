def maxArea(heights: list[int]) -> int:
	area = 0
	a = 0
	b = len(heights) - 1

	while a < b:
		area = max(area, (b - a) * min(heights[a], heights[b]))
		if heights[a] <= heights[b]:
			a += 1
		elif heights[a] > heights[b]:
			b -= 1

	return area 
	
