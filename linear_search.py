def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  
    return -1 

my_list = [2, 4, 7, 1, 9, 3, 6]
target_value = 9

result = linear_search(my_list, target_value)

if result != -1:
    print(f"Element {target_value} is present at index {result}.")
else:
    print(f"Element {target_value} is not present in the list.")
