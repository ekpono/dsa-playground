"""
The num does does all the pre and decrement,
Once the num is 10, the num now becomes available to post recursion in incremental manner
"""
# 20
# 19
# 18
# 17
# 16
# 15
# 14
# 13
# 12
# 11
# ======
# 11
# ======
# 12
# ======
# 13
# ======
# 14
# ======
# 15
# ======
# 16
# ======
# 17
# ======
# 18
# ======
# 19
# ======
# 20
# def subtr(num):
#     if num == 10:
#         return 10
#
#     print(num)
#
#     result = num - subtr(num - 1)
#     print("======")
#
#     print(num)
#     return result
# re = subtr(20)


def subtr(num):
    if num == 10:
        return 10

    # result = num - subtr(num - 1)

    return num - subtr(num - 1)
re = subtr(20)
print(re)