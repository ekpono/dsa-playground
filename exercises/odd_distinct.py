def oddDistinct(array):
        hash = dict()


        for i in range(0, len(array) -1):
                if array[i] % 2 != 0:
                        if array[i] in hash:
                                hash[array[i]] = False
                        else:
                                hash[array[i]] = True
        
        return True in hash.values()


array = [2,3,4,5,2,1,3,1,5]
result = oddDistinct(array)

print(result)
