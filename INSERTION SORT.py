def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1
        # Move elements that are greater than key to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Place the key at its correct position
        arr[j + 1] = key   

# Define the array
arr = [9,7,25,23,6]  
 # Print original array
print("Original array:", arr)  
# Call the insertion sort function
insertion_sort(arr)   
 # Print sorted array
print("Sorted array:", arr)  
