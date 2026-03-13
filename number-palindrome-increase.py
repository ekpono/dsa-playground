def palindrome(num):
	if str(num) == "".join(reversed(str(num))):
		return num


	return palindrome(num + 1)


print(palindrome(1200))