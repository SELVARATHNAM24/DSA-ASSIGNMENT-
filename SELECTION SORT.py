def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in unsorted array
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Define the array
arr = [64, 25, 12, 22, 11] 
# Print original array
print("Original array:", arr)   
# Call the selection sort function
selection_sort(arr)  
# Print sorted array
print("Sorted array:", arr)  
