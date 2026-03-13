def dot_notation(a, b):
        if (len(a) != len(b)):
                raise ValueError('Value are not the same length')
        c = []

        for i in range(len(a)):
                c.append(a[i] * b[i])
        
        return c

result = dot_notation([1,2,3,4], [7,6,7,8])

print(result)
