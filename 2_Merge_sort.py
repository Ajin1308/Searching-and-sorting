#time complexity O(nlogn)

def merge_sort(array):
    if len(array) <= 1:
        return array
        
    middle = len(array) // 2 
    left_half = merge_sort(array[:middle])
    right_half = merge_sort(array[middle:])

    return merge(left_half, right_half)

def merge(left , right):
    result =[]
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    result += left[i:]
    result += right[j:]

    return result

my_array = [9, 4, 7, 2, 1, 5, 3, 8, 6,1]
sorted_array = merge_sort(my_array)
print("Sorted array:", sorted_array)