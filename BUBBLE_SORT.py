arr = [97, 60, 45, 96, 33, 19, 53, 37, 29, 98]

def sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

sort(arr)
print(arr)
