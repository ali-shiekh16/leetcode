def two_sum(nums, target):
	low, high = 0, len(nums) - 1

	while low < high:
		sum = nums[low] + nums[high] 
		if sum == target:
			return [low + 1, high + 1]

		if sum < target:
			low += 1
		else:
			high -= 1

	return [-1, -1]


nums = [3, 2, 4]
print(two_sum(nums, 6))
		

