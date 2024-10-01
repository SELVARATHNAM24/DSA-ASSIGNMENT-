def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
         for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

 # Define the array 
arr = [64, 34, 25, 12, 22, 11, 90]  
# Print original array before sorting
print("Original array:", arr)   
# Call the bubble sort function
bubble_sort(arr)   
 # Print sorted array 
print("Sorted array:", arr)  