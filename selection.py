
def selectionSort(arr, n):
    for i in range(0, n):
        min_index = i
        for j in range(i, n):
            if(arr[min_index]> arr[j]):
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


arr = [64,25,36,25,14,20]
n = len(arr)

selectionSort(arr, n)
print(arr)