def partition(arr, low, high):
    # 1. Choose the rightmost element as the pivot
    pivot = arr[high]

    # 2. Pointer for the greater element
    i = low - 1

    # 3. Compare each element with the pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            # If element smaller than pivot is found, swap it with the greater element pointed by i
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    # 4. Swap the pivot element with the greater element specified by i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # 5. Return the position where the partition is done
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # Find pivot element such that element smaller than pivot are on left
        # and elements greater than pivot are on right
        pi = partition(arr, low, high)

        # Recursive call on the left of pivot
        quick_sort(arr, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(arr, pi + 1, high)


# --- Test the Code ---
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
print("Original array:", my_array)

n = len(my_array)
quick_sort(my_array, 0, n - 1)

print("Sorted array:  ", my_array)