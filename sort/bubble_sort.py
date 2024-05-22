
def bubbleSor(arr):
    n = len(arr)
    swapped = False
    for i in range(n):

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

