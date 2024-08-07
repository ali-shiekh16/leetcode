def encode(strs):
	encoded = ''
	for word in strs:
		encoded += str(len(word)) + '#' + word 
	return encoded 


def decode(s):
	decoded = []
	start = 0
	for i in range(len(s)):
		if s[i] == '#' and s[i - 1].isdigit():
			n = ''
			for j in range(start, i):
				n += s[j]
			
			decoded.append(s[i + 1:i + int(n) + 1])	
			print(decoded)
			start = i + int(n) + 1
			i = start

	return decoded	

# print(decode(encode(['neet', 'code', 'love', 'you'])))
s = '12345'
print(s[1:3])