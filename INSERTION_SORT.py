arr = [97, 60, 45, 96, 33, 19, 53, 37, 29, 98]

def insertion_sort(arr):
    for index in range(1, len(arr)):
        value = arr[index]
        i = index - 1
        while  i >= 0:
            if value < arr[i]:
                arr [i + 1] = arr [i]
                arr[i] = value
                i = i - 1
            else:
                break

insertion_sort(arr)
print(arr)
    
