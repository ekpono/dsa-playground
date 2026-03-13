def sequence(string, k):
        n = len(string) 
        j = k + n

        return string[k], string[j]


result = sequence('ekpeudisijsxl', -5)
print(result)