def unique(array):
        hash = {}
        distinct = True

        for i in array:
                if i in hash:
                        distinct = False
                        break
                else:
                        hash[i] = True
        
        return distinct


result = unique([1,2,3,4,5,6])

print(result)