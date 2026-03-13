def vowels():
        all_vowels = ['a', 'e', 'i', 'o', 'u']

        words = 'Ekpono Is A Great Man'

        totalVowels = 0

        for word in words:
                if word.lower() in all_vowels:
                        totalVowels += 1
        
        return totalVowels

result = vowels()
print(result)