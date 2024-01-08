def min_sum_of_product(arr1, arr2):
    if not arr1 or not arr2 or len(arr1) != len(arr2):
        return None

    arr1.sort()
    arr2.sort(reverse=True)

    min_sum = 0
    for i in range(len(arr1)):
        min_sum += arr1[i] * arr2[i]

    return min_sum

# Example arrays
array1 = [2, 1, 6, 9, 4]
array2 = [5, 4, 7, 2, 8]

result = min_sum_of_product(array1, array2)
print("Minimum sum of product:", result)
