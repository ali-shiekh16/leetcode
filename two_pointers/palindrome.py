def isPalindrome(s):
	start = 0
	end = len(s) -1 

	while start < end:
		while not isAlphaNum(s[start]) and start < len(s):
			start += 1

		while not isAlphaNum(s[end]) and end >= 0:
			end -= 1

		if s[start].lower() != s[end].lower():
			return False

		start += 1
		end -= 1

	return True

def isAlphaNum(c):
	return (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')

s = "tac a .cat!"
print(isPalindrome(s))

