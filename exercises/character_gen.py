def generateCharacters():
        result = []
        for i in range(97, 123):
                result.append(chr(i) + ' ')
        
        return result

result = generateCharacters()
print(result)

print(ord('a'))