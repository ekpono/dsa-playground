def palindrome(word):
        word = word.lower()
        return word[::-1] == word

word = 'MOm'
result = palindrome(word)
print(result)