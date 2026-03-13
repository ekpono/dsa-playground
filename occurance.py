def count_character_occurance(words):
        hash = {}

        for word in words:
                if word in hash:
                        hash[word] = hash[word] + 1
                else:
                        hash[word] = 1
        
        print(hash)


word = 'hellpppp'
count_character_occurance(word)