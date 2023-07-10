#time complexity is O(n^2)

def insertion_sort(array):
    if len(array) <= 1:
        return array

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] =  array[j]
            j = j - 1
        array[j + 1] = key

    return array
    
sort = insertion_sort([214,565,1,25,643,613,7453,16])
print(sort)