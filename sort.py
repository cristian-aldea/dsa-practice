from heapq import merge
import random
import time

import matplotlib.pyplot as plt


def bubble_sort(arr):
    # swap two numbers if in wrong order
    # keep swapping until everything is sorted
    swapped = True
    while True:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        if not swapped:
            break


def selection_sort(arr):
    # find smallest, swap with first
    # find second smallest, swap with second
    # continue until sorted
    for i in range(len(arr)-1):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]


def insertion_sort(arr):
    # there are two sections: sorted and unsorted
    # take a card from the unsorted section and insert it into right place
    for i in range(len(arr)):
        value = arr[i]
        j = i-1
        while j >= 0 and arr[j] > value:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = value


def merge_sort(arr):
    # recursive
    # split array into 2 
    # sort sub arrays
    # merge the two sorted arrays
    # when merging, keep track of two points for l and r
    # add smallest of two pointers to result, increment pointer

    if len(arr) <= 1:
        return

    mid = len(arr)//2

    l = arr[:mid]
    r = arr[mid:]

    merge_sort(l)
    merge_sort(r)

    ri, li, ai = 0, 0, 0

    while ri < len(r) and li < len(l):
        if l[li] < r[ri]:
            arr[ai] = l[li]
            li += 1
        else:
            arr[ai] = r[ri]
            ri += 1
        ai += 1

    while ri < len(r):
        arr[ai] = r[ri]
        ai += 1
        ri += 1

    while li < len(l):
        arr[ai] = l[li]
        ai += 1
        li += 1


def quick_sort(arr):
    # pick a pivot (first element)
    # partition array into 2
    # elements < than pivot go to the left, > go to the right
    # use two pointers and swap when needed
    # repeat recursively until sorted
    quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, start, end):
    if start > end:
        return

    p = partition(arr, start, end)

    quick_sort_helper(arr, start, p-1)
    quick_sort_helper(arr, p+1, end)


def partition(arr, start, end):
    n = len(arr)

    # pi = random.randint(start, end)
    # arr[start], arr[pi] = arr[pi], arr[start]
    pi = start
    pivot = arr[pi]

    while start < end:

        while start < n and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    arr[pi], arr[end] = arr[end], arr[pi]

    return end


if __name__ == "__main__":
    arr = [random.randint(0, 10) for _ in range(1000)]
    print("Sorting test array")
    quick_sort(arr)
    print("Sorted?:", sorted(arr) == arr)

    print("Timing sorting at various array sizes")
    arr_lengths = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 3000, 4000, 5000]
    # bubble sort too slow lmao
    algos = [selection_sort, insertion_sort, merge_sort, quick_sort]
    labels = [algo.__name__ for algo in algos]

    times = [None] * len(algos)

    for n in arr_lengths:
        for i, algo in enumerate(algos):
            print(f"Timing {labels[i]} for size {n}")
            arr = [random.randint(0, 100) for _ in range(n)]

            start_time = time.time()
            algo(arr)
            time_taken = time.time() - start_time
            if not times[i]:
                times[i] = []
            times[i].append(time_taken)

    for i, t in enumerate(times):
        plt.plot(arr_lengths, t, label=labels[i])
    plt.title("Sorting time vs. array length")
    plt.legend()
    plt.show()
