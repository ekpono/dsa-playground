from random import randint

def shuffle(array):
        shuff = []
        leng = len(array)

        def generaterNewIndex(start, stop):
                result = randint(start, stop)

                return result

        for i in range(0, leng ):
                newIndex = generaterNewIndex(0, leng -1)
                # array[i], array[newIndex] = array[newIndex], array[i]
                shuff.append(array[newIndex])
        
        return shuff

data = [1,2,3,4,5,6,7]

result = shuffle(data);
print(data)
print(result)
