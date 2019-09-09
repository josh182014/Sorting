# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    swaps_occurred = True
    while swaps_occurred:
        swaps_occurred = False
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
                swaps_occurred = True
    return arr


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr


if __name__ == "__main__":
    print(f"Selection Sort: [4, 2, 5, 1]")
    print(selection_sort([4, 2, 5, 1]))
    print(f"Bubble Sort: [4, 2, 5, 1]")
    print(bubble_sort([4, 2, 5, 1]))
