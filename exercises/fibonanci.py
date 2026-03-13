def fibonnic(n):
        result = list()
        for i in range(0, n + 1, 1):
                result.append(i)
        
        return result

result = fibonnic(256)
print(result)