def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    
    left = []
    right = []
    
    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print(sorted_arr)
