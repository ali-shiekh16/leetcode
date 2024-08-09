def longestConsecutive(nums):
	vals = set(nums)	
	longest = 0

	for n in vals:
		if n - 1 in vals:
			continue

		length = 1
		while n + length in vals:
			length += 1

		longest = max(longest, length)

	return longest


print(longestConsecutive([0,3,2,5,4,6,1,1]))


