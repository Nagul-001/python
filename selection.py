arr=[5,4,3,2,1]
for i in range(0,len(arr)-1):
    minimum=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[minimum]:
            minimum=j
    arr[i],arr[minimum]=arr[minimum],arr[i]
print(arr)
    

