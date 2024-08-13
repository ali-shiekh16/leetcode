def trap(height: list[int]) -> int:
	area = 0
	left, right = 0, len(height) - 1
	leftMax, rightMax = height[0], height[-1]

	if len(height) == 0:
		return area

	while left < right:
		if height[left] <= height[right]:
			rain = leftMax - height[left]
			area += rain if rain > 0 else 0
			left += 1
			leftMax = max(height[left],leftMax)

		else:
			rain = rightMax - height[right]
			area += rain if rain > 0 else 0
			right -= 1
			rightMax = max(height[right], rightMax)

	return area



heights = [0,2,0,3,1,0,1,3,2,1]
print(trap(heights))