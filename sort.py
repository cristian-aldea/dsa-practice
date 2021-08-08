import random
import time

import matplotlib.pyplot as plt


def bubble_sort(arr):

    swapped = True
    while True:
        swapped = False

        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                # temp = arr[i]; arr[i] = arr[i+1]; arr[i+1] = temp
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        if not swapped:
            break


def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]


def insertion_sort(arr):

    for i in range(len(arr)):
        value = arr[i]

        j = i-1
        while j >= 0 and arr[j] > value:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = value


def merge_sort(arr):
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


arr = [random.randint(0, 10) for _ in range(1000)]

print("Before:", arr)
# bubble_sort(arr)
# selection_sort(arr)
# insertion_sort(arr)
# merge_sort(arr)
quick_sort(arr)
print("After: ", arr)
print("Sorted:", sorted(arr) == arr)


n_orders = [1, 10, 20, 50, 100, 200, 500, 1000, 2000,
            3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

x = []
y = []
for i in n_orders:
    arr = [random.randint(0, 10) for _ in range(i)]
    print(len(arr))

    start_time = time.time()
    quick_sort(arr)
    time_taken = time.time() - start_time
    x.append(len(arr))
    y.append(time_taken)

plt.plot(x, y)
plt.show()
