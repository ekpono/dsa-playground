def removePunctuation(s):
        return ''.join(char for char in s if char.isalpha() or char.isspace()) #chatgpt result

        # My result

        # result = []
        # allCharacts = []

        # for pu in range(97, 123):
        #         allCharacts.append(chr(pu))

        # for i in range(len(s)):
        #         if s[i].lower() in allCharacts or s[i] == " ":
        #                 result.append(s[i])
                
        # return ''.join(result)
        

result = removePunctuation("Let's try, Mike")
print(result)
