#Todo  sort and turn it back to string ''.join(sorted('ekpono'))
def anagram(source, target):
        return sorted(source.lower()) == sorted(target.lower())
        


word1 = 'Cinema'
word2 = 'iceman'

result = anagram(word1, word2)
print(result)