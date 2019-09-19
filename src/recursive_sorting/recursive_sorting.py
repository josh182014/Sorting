# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    left, right = 0, 0
    for i in range(elements):
        if left >= len(arrA):
            merged_arr.insert(i, arrB[right])
            merged_arr.pop(i + 1)
            right += 1
        elif right >= len(arrB):
            merged_arr.insert(i, arrA[left])
            merged_arr.pop(i + 1)
            left += 1
        elif arrA[left] < arrB[right]:
            merged_arr.insert(i, arrA[left])
            merged_arr.pop(i + 1)
            left += 1
        else:
            merged_arr.insert(i, arrB[right])
            merged_arr.pop(i + 1)
            right += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])
    arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


if __name__ == "__main__":
    print(merge_sort([3, 3, 2, 5, 6, 4, 9, 6]))
