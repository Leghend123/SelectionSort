#implementation of selection sort algorithm

#function for the sorting -------
def select_sort(arr):
    #tranvese through the array element 
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
            arr[i],arr[min_index] = arr[min_index],arr[i]


if __name__ == "__main__":
    print("Enter the array:")
    arr = list(map(int,input().split()))
    select_sort(arr)
    print("-----------------")
    print("Sorted array:")
    for i in range(len(arr)):
        print("%d " %arr[i], end=" ")



