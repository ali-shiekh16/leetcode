def three_sum(nums):
	result = []
	nums.sort()

	for i, n in enumerate(nums):
		if i > 0 and n == nums[i-1]:
			continue

		low, high = i+1, len(nums)-1

		while low < high:
			three_sum = n + nums[low] + nums[high]

			if three_sum > 0:
				high -= 1

			elif three_sum < 0:
				low += 1

			else:
				result.append([n, nums[low], nums[high]])

				low += 1
				while low < high and nums[low] == nums[low-1]:
					low += 1

	return result 


input = [-1,0,1,2,-1,-4]
print(three_sum(input))