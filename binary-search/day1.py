def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        print('mid', mid)
        
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            print("left", mid, arr[mid])
            left = mid + 1
        else:
            print("right", mid, arr[mid])
            right = mid - 1
    
    return -1  # Target not found


# Sample sorted array and target
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 2

# Iterative binary search
result_iterative = binary_search_iterative(arr, target)
print(f"Iterative approach: Index of {target} is {result_iterative}")