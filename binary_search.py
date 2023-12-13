def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  
        elif mid_value < target:
            low = mid + 1  
        else:
            high = mid - 1  

    return -1 

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 11

result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Element {target_value} is present at index {result}.")
else:
    print(f"Element {target_value} is not present in the array.")
