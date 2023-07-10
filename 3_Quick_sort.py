# Time complexity = O(nlogn)
# Space complexity = o(n)
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)


array = [5,4,6,7,1,2,0,9]
quick_sort(array,0,len(array)-1)
print(array)

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#         left = [i for i in array[1:] if i < pivot]
#         right = [i for i in array[1:] if i >= pivot]
#         quick_sort(left) + (pivot) + (right)
# # (Time complexity = O(n^2))
