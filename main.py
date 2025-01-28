def bubble_sort(arr):
    for x in range(len(arr)):
        swap=False
        for i in range(len(arr)-x-1):
            if(arr[i]>arr[i+1]):
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
                swap=True
        if not swap:
            break
arr=[5,4,3,1,2]
bubble_sort(arr)
print(arr)