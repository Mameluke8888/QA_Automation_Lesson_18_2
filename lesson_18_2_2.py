# Exercise #2
# Write a python code for Quick sort algorithm when the last element is used as a pivot.
# You can use the example from the video, but all solutions from the internet will be rejected.


def partition(array, start, end):
    pivot = array[end]
    low = start
    high = end - 1

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            temp = array[low]
            array[low] = array[high]
            array[high] = temp
        else:
            break

    array[end] = array[low]
    array[low] = pivot

    return low


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


array = [29, 99, 27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]
quick_sort(array, 0, len(array) - 1)
print(array)
