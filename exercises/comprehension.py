def compreshension(n):
        if n == 1:
                return [n];

        result = [n]

        result.extend(compreshension(n//2))

        return result

result = compreshension(256)
print(result)