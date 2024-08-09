# https://leetcode.com/problems/top-k-frequent-elements/description/
def topKFrequent(nums, k):
	freq = {}
	for i in nums:
			if i in freq:
					freq[i] += 1
			else:
					freq[i] = 1
			
	sorted_nums = [[] for x in range(len(nums) + 1)]

	for key, value in freq.items():
		sorted_nums[value].append(key)


	result = []

	for i in range(len(sorted_nums) - 1):
			n = sorted_nums[len(sorted_nums) - 1 - i]
			if len(n):
				for j in n:
					if k == 0:
						return result
					result.append(j)
					k -= 1

	return result 


print(topKFrequent([1, 1, 1, 2, 2, 3], 1))