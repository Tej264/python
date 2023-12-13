def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

my_list = [64, 34, 25, 12, 22, 11, 90]
print("Original List:", my_list)

insertion_sort(my_list)
print("Sorted List:", my_list)