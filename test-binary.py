def binary_tree(arr, target):
	left = 0
	right = len(arr) - 1

	while (left <= right):
		mid = (left + right) // 2

		if (arr[mid] == target):
			return mid;
		elif (arr[mid] < target):
			left = left + 1
		else:
			right = right - 1
	return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 13

print(binary_tree(arr, target))
