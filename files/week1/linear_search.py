def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        return -1


arr = [3, 4, 5, 6, 7, 3, 2, 5, 4, 9]
print(arr)
target = int(input("Enter the number to search: "))
target_val_index = linear_search(arr,target)
if target_val_index != -1:
  print(f"The target value {arr[target_val_index]} found at index {target_val_index}  ")