from random import randrange

def choice(array):
        randIndex = randrange(0, len(array))

        return array[randIndex]


result = choice([20, 30, 10, 4, 1, 80, 17, 29, 18])
print(result)