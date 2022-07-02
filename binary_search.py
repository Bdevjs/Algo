def binarysearch(arr, low, high, k):
    if(high>=low):
        mid = (high + low) // 2
        if(arr[mid] == k):
            return mid
        elif (arr[mid]> k):
            return binarysearch(arr, low, mid-1, k)
        else:
            return binarysearch(arr, mid+1, high, k)

    else:
        return -1


n = int(input("Enter the number of Array:"))
arr = list (map(int,input("Enter Array list - ").strip().split()))


arr.sort()
print(arr);

k = int(input("Enter your keyword: "))

result = binarysearch(arr, 0, len(arr)-1, k)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

    