def factor(n):
        k = 1

        while k * k < n:
                if n % k == 0:
                        yield k
                        # yield n // k
                k += 1
        if k * k == n:
                yield k

        k -= 1
        while k > 0:
                if n % k == 0:
                        if k != n // k:
                                yield n // k
                        else:
                                print(k != n // k)
                                print(k, n // k)
                k -= 1



        



result = factor(100)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# def fibonnaci():
#         a = 0
#         b = 1
#         result = []
#         while a < 100:
#                 yield a
#                 future = a + b
#                 a = b
#                 b = future
        
#         return result
        
# result = fibonnaci()
# print(result)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
