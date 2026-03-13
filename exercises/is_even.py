def isEven(k):
        result = divmod(k, 2)

        [div, reminder] = result

        return reminder == 0

result = isEven(13)
print(result)