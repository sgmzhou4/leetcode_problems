def quickSort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    left = [x for x in array if x < pivot]
    mid = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quickSort(left) + mid + quickSort(right)

array = [2,3,0,9,5,2,7,4,78,41,24,900]
print(quickSort(array))