def mergeSort(array):
    if len(array) < 2:
        return array
    mid = len(array)//2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return merge(left,right)

def merge(left,right):
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res

array = [0,2,5,1,3,8,5,6,9]
print(mergeSort(array))